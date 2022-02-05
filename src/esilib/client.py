from pathlib import Path
from typing import List, Union
from esilib.security import ESISecurity


class ESIClient:
    security: ESISecurity

    def __init__(
        self,
        client_id: str,
        permissions: List[str],
        auth_url: str = None,
        token_url: str = None,
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

        self.security = ESISecurity(**kwargs)
