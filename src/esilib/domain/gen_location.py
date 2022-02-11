import json
from typing import List
from esilib.domain.base_domain import BaseDomain
from esilib.exceptions import UnknownAPIStatus
from esilib.models import ESIResponse, ESIResponseMeta


'''
THIS FILE HAS BEEN GENERATED AUTOMATICALLY.
PLEASE DO NOT MODIFY IT DIRECTLY.
'''


class Location(BaseDomain):
    '''
    ESI API version 1.10.1
    '''
    BASE_PATH = '/latest'

    def get_characters_character_id_location(
        self,
        character_id: int,
        datasource: str = 'tranquility',
        token: str = None,
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Information about the characters current location. Returns the current solar system id, and also the current station or structure ID if applicable

        ---
        Alternate route: `/dev/characters/{character_id}/location/`

        Alternate route: `/legacy/characters/{character_id}/location/`

        Alternate route: `/v1/characters/{character_id}/location/`

        Alternate route: `/v2/characters/{character_id}/location/`

        ---
        This route is cached for up to 5 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param token str: DESCRIPTION
        :param character_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'token': token}
        path_params = {'character_id': character_id}

        url = f'/characters/{character_id}/location/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_characters_character_id_online(
        self,
        character_id: int,
        datasource: str = 'tranquility',
        token: str = None,
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Checks if the character is currently online

        ---
        Alternate route: `/dev/characters/{character_id}/online/`

        Alternate route: `/v2/characters/{character_id}/online/`

        Alternate route: `/v3/characters/{character_id}/online/`

        ---
        This route is cached for up to 60 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param token str: DESCRIPTION
        :param character_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'token': token}
        path_params = {'character_id': character_id}

        url = f'/characters/{character_id}/online/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_characters_character_id_ship(
        self,
        character_id: int,
        datasource: str = 'tranquility',
        token: str = None,
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Get the current ship type, name and id

        ---
        Alternate route: `/dev/characters/{character_id}/ship/`

        Alternate route: `/legacy/characters/{character_id}/ship/`

        Alternate route: `/v1/characters/{character_id}/ship/`

        Alternate route: `/v2/characters/{character_id}/ship/`

        ---
        This route is cached for up to 5 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param token str: DESCRIPTION
        :param character_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'token': token}
        path_params = {'character_id': character_id}

        url = f'/characters/{character_id}/ship/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)
