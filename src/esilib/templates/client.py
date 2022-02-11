from pathlib import Path
from typing import List, Union
from esilib.security import ESISecurity
~~IMPORTS~~


class ESIClient:
    security: ESISecurity
    endpoint_url: str

    def __init__(
        self,
        client_id: str,
        permissions: List[str],
        auth_url: str = None,
        token_url: str = None,
        endpoint_url: str = None,
        auth_callback_html: Union[str, Path] = None,
    ) -> None:
        kwargs = {
            'client_id': client_id,
            'permissions': permissions,
        }

        if auth_url:
            kwargs['auth_url'] = auth_url
        if token_url:
            kwargs['token_url'] = token_url
        if auth_callback_html:
            kwargs['auth_callback_html'] = auth_callback_html

        self.security = ESISecurity(
            client_id=client_id,
            permissions=permissions,
            auth_url=auth_url,
            token_url=token_url,
            auth_callback_html=auth_callback_html,
        )

        self.endpoint_url = endpoint_url

    def login(self) -> None:
        self.security.login()

    def _get_domain(self, name: str, cls: type):
        attr = f'_{name}'
        if not hasattr(self, attr):
            setattr(self, attr, cls(self.security))

        return getattr(self, attr)
