import json
from typing import List
from esilib.domain.base_domain import BaseDomain
from esilib.exceptions import UnknownAPIStatus
from esilib.models import ESIResponse, ESIResponseMeta


'''
THIS FILE HAS BEEN GENERATED AUTOMATICALLY.
PLEASE DO NOT MODIFY IT DIRECTLY.
'''


class Search(BaseDomain):
    '''
    ESI API version 1.10.1
    '''
    BASE_PATH = '/latest'

    def get_characters_character_id_search(
        self,
        character_id: int,
        categories: List[str],
        search: str,
        datasource: str = 'tranquility',
        language: str = 'en',
        strict: bool = None,
        token: str = None,
        accept_language: str = 'en',
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Search for entities that match a given sub-string.

        ---
        Alternate route: `/dev/characters/{character_id}/search/`

        Alternate route: `/legacy/characters/{character_id}/search/`

        Alternate route: `/v3/characters/{character_id}/search/`

        ---
        This route is cached for up to 3600 seconds

        :param accept_language str: DESCRIPTION
        :param etag str: DESCRIPTION
        :param categories List[str]: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param language str: DESCRIPTION
        :param search str: DESCRIPTION
        :param strict bool: DESCRIPTION
        :param token str: DESCRIPTION
        :param character_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'Accept-Language': accept_language, 'If-None-Match': etag}
        query_params = {'categories': categories, 'datasource': datasource,
                        'language': language, 'search': search, 'strict': strict, 'token': token}
        path_params = {'character_id': character_id}

        url = f'{self.BASE_URI}/characters/{character_id}/search/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_search(
        self,
        categories: List[str],
        search: str,
        datasource: str = 'tranquility',
        language: str = 'en',
        strict: bool = None,
        accept_language: str = 'en',
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Search for entities that match a given sub-string.

        ---
        Alternate route: `/dev/search/`

        Alternate route: `/legacy/search/`

        Alternate route: `/v2/search/`

        ---
        This route is cached for up to 3600 seconds

        :param accept_language str: DESCRIPTION
        :param etag str: DESCRIPTION
        :param categories List[str]: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param language str: DESCRIPTION
        :param search str: DESCRIPTION
        :param strict bool: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'Accept-Language': accept_language, 'If-None-Match': etag}
        query_params = {'categories': categories, 'datasource': datasource,
                        'language': language, 'search': search, 'strict': strict}
        path_params = {}

        url = f'{self.BASE_URI}/search/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)
