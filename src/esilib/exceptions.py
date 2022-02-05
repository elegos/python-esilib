from datetime import datetime
from email.utils import parsedate
import json
import time
from typing import Any, Dict

import requests

from esilib.models import ESIResponseMeta


class ESIException(Exception):
    pass


class UnknownAPIStatus(ESIException):
    def __init__(self, response: requests.Response) -> None:
        super().__init__(f'Unknown ESI API status (status code: {response.status_code})')


class ESIBaseError(ESIException):
    error: str

    _json_response: Dict[str, Any]

    def __init__(self, response: requests.Response) -> None:
        self._json_response = json.loads(response.content)

        super().__init__(self._json_response['error'])


class NotModified(ESIException):
    meta: ESIResponseMeta

    def __init__(self, response: requests.Response) -> None:
        super().__init__()

        self.meta = ESIResponseMeta(response)


class BadRequest(ESIBaseError):
    pass


class ErrorLimited(ESIBaseError):
    pass


class InternalServerError(ESIBaseError):
    pass


class ServiceUnavailable(ESIBaseError):
    pass


class GatewayTimeout(ESIBaseError):
    timeout: int

    def __init__(self, response: requests.Response) -> None:
        super().__init__(response)

        self.timeout = self._json_response['timeout']
