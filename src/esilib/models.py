from dataclasses import dataclass
from datetime import datetime
from email.utils import parsedate
import time
from typing import Any, Generic, List, TypeVar

import requests

T = TypeVar('T')


class ESIResponseMeta:
    cache_control: str
    etag: str
    expires: datetime
    last_modified: datetime

    def __init__(self, response: requests.Response) -> None:
        self.cache_control = response.headers['cache-control']
        self.etag = response.headers['etag']
        self.expires = datetime.fromtimestamp(time.mktime(parsedate(response.headers['expires'])))
        self.last_modified = datetime.fromtimestamp(
            time.mktime(parsedate(response.headers['last-modified'])))


@dataclass
class ESIResponse(Generic[T]):
    meta: ESIResponseMeta
    data: T


class ESIListResult(ESIResponse, Generic[T]):
    data: List[T]
