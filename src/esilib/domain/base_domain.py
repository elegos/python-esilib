from typing import Any, Dict
from esilib.exceptions import BadRequest, ErrorLimited, GatewayTimeout, InternalServerError, NotModified, ServiceUnavailable
from esilib.security import ESISecurity

import requests


class BaseDomain:
    endpoint_url: str
    security: ESISecurity

    def __init__(self, security: ESISecurity, endpoint_url: str = None) -> None:
        self.endpoint_url = endpoint_url or 'https://esi.evetech.net/latest'
        if self.endpoint_url.endswith('/'):
            self.endpoint_url = self.endpoint_url[:-1]
        self.security = security

    @staticmethod
    def _manage_generic_response_status_code(response: requests.Response):
        if response.status_code == 304:
            raise NotModified(response)

        if response.status_code == 400:
            raise BadRequest(response)

        if response.status_code == 420:
            raise ErrorLimited(response)

        if response.status_code == 500:
            raise InternalServerError(response)

        if response.status_code == 503:
            raise ServiceUnavailable(response)

        if response.status_code == 504:
            raise GatewayTimeout(response)

    def _get(
        self,
        uri: str,
        uri_tokens: Dict[str, Any] = None,
        query_params: Dict[str, Any] = None,
        headers: Dict[str, str] = None,
    ) -> requests.Response:
        '''
        :raises esilib.models.exceptions.BadRequest
        :raises esilib.models.exceptions.ErrorLimited
        :raises esilib.models.exceptions.InternalServerError
        :raises esilib.models.exceptions.ServiceUnavailable
        :raises esilib.models.exceptions.GatewayTimeout
        '''
        url = f'{self.endpoint_url}{uri}'.format(**(uri_tokens or {}))

        response = requests.get(
            url=url,
            params=query_params,
            headers={
                'Authorization': f'Bearer {self.security.access_token}',
                **(headers or {})
            }
        )

        self._manage_generic_response_status_code(response)

        return response
