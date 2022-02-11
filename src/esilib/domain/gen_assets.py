import json
from typing import List
from esilib.domain.base_domain import BaseDomain
from esilib.exceptions import UnknownAPIStatus
from esilib.models import ESIResponse, ESIResponseMeta


'''
THIS FILE HAS BEEN GENERATED AUTOMATICALLY.
PLEASE DO NOT MODIFY IT DIRECTLY.
'''


class Assets(BaseDomain):
    '''
    ESI API version 1.10.1
    '''
    BASE_PATH = '/latest'

    def get_characters_character_id_assets(
        self,
        character_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Return a list of the characters assets

        ---
        Alternate route: `/dev/characters/{character_id}/assets/`

        Alternate route: `/v5/characters/{character_id}/assets/`

        ---
        This route is cached for up to 3600 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param page int: DESCRIPTION
        :param token str: DESCRIPTION
        :param character_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'page': page, 'token': token}
        path_params = {'character_id': character_id}

        url = f'/characters/{character_id}/assets/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_assets(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Return a list of the corporation assets

        ---
        Alternate route: `/dev/corporations/{corporation_id}/assets/`

        Alternate route: `/v5/corporations/{corporation_id}/assets/`

        ---
        This route is cached for up to 3600 seconds

        ---
        Requires one of the following EVE corporation role(s): Director


        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param page int: DESCRIPTION
        :param token str: DESCRIPTION
        :param corporation_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'page': page, 'token': token}
        path_params = {'corporation_id': corporation_id}

        url = f'/corporations/{corporation_id}/assets/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)
