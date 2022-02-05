import base64
import json
import secrets
import urllib.parse
import webbrowser
from datetime import datetime, timedelta
from hashlib import sha256
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from typing import List, Union

import requests

AUTH_SERVER_PORT = 55533


class ESISecurity:
    client_id: str
    auth_url: str
    token_url: str
    permissions: List[str]
    auth_callback_html: str

    code_verifier: str
    state_csrf: str
    auth_code: str

    access_token: str
    refresh_token: str
    access_token_expiry_date: datetime

    def __init__(
        self,
        client_id: str,
        permissions: List[str],
        auth_url: str = 'https://login.eveonline.com/v2/oauth/authorize/',
        token_url: str = 'https://login.eveonline.com/v2/oauth/token',
        auth_callback_html: Union[str, Path] = 'You can now close this window',
    ) -> None:
        self.client_id = client_id
        self.permissions = permissions
        self.auth_url = auth_url
        self.token_url = token_url
        self.auth_callback_html = auth_callback_html

        self.access_token = None
        self.refresh_token = None
        self.access_token_expiry_date = None

        if isinstance(self.auth_callback_html, Path):
            self.auth_callback_html = self.auth_callback_html.read_text()

        code_verifier = secrets.token_bytes(32)

        self.code_verifier = base64.urlsafe_b64encode(code_verifier).decode('utf-8').rstrip('=')

    def _challenge_code(self) -> str:
        return base64.urlsafe_b64encode(sha256(self.code_verifier.encode('utf-8')).digest()) \
            .decode('utf-8').rstrip('=')

    def _sso_handler_factory(self) -> type:
        class SSOHandler(SimpleHTTPRequestHandler):
            def log_message(self, format, *args):
                pass

            def do_GET(this):
                parsed_path = urllib.parse.urlparse(this.path)
                query_params = urllib.parse.parse_qs(parsed_path.query)
                self.auth_code = query_params['code'][0]

                this.send_response(200)
                this.end_headers()
                this.wfile.write(self.auth_callback_html.encode('utf-8'))

        return SSOHandler

    def _register_access_token(self, token_response: requests.Response) -> None:
        token_data = json.loads(token_response.content)

        self.access_token = token_data['access_token']
        self.refresh_token = token_data['refresh_token']
        self.access_token_expiry_date = datetime.now() + timedelta(
            seconds=token_data['expires_in']
        )

    def login(self) -> None:
        '''
        Login via SSO (mobile/desktop method)
        https://docs.esi.evetech.net/docs/sso/native_sso_flow.html
        '''

        self.state_csrf = secrets.token_hex()

        query_params = {
            'response_type': 'code',
            'redirect_uri': f'http://localhost:{AUTH_SERVER_PORT}',
            'client_id': self.client_id,
            'scope': urllib.parse.quote(' '.join(self.permissions)),
            'code_challenge': urllib.parse.quote(self._challenge_code()),
            'code_challenge_method': 'S256',
            'state': self.state_csrf,
        }
        query_params = [f'{key}={value}' for key, value in query_params.items()]
        webbrowser.open(f'{self.auth_url}?{"&".join(query_params)}')

        with HTTPServer(('localhost', AUTH_SERVER_PORT), self._sso_handler_factory()) as httpd:
            httpd.handle_request()

        token_response = requests.post(self.token_url, headers={
            'Content-Type': 'application/x-www-form-urlencoded',
        }, data={
            'grant_type': 'authorization_code',
            'code': self.auth_code,
            'client_id': self.client_id,
            'code_verifier': self.code_verifier,
        })

        self._register_access_token(token_response)

    def refresh(self) -> None:
        '''
        Refresh the access token
        https://docs.esi.evetech.net/docs/sso/refreshing_access_tokens.html#native-applications
        '''

        if not self.refresh_token:
            raise Exception('You need to login first.')

        response = requests.post(self.token_url, headers={
            'Content-Type': 'application/x-www-form-urlencoded',
        }, data={
            'grant_type': 'refresh_token',
            'refresh_token': self.refresh_token,
            'client_id': self.client_id,
        })

        self._register_access_token(response)
