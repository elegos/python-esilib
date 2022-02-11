import json
from typing import List
from esilib.domain.base_domain import BaseDomain
from esilib.exceptions import UnknownAPIStatus
from esilib.models import ESIResponse, ESIResponseMeta


'''
THIS FILE HAS BEEN GENERATED AUTOMATICALLY.
PLEASE DO NOT MODIFY IT DIRECTLY.
'''


class Fleets(BaseDomain):
    '''
    ESI API version 1.10.1
    '''
    BASE_PATH = '/latest'

    def get_characters_character_id_fleet(
        self,
        character_id: int,
        datasource: str = 'tranquility',
        token: str = None,
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Return the fleet ID the character is in, if any.

        ---
        Alternate route: `/legacy/characters/{character_id}/fleet/`

        Alternate route: `/v1/characters/{character_id}/fleet/`

        ---
        This route is cached for up to 60 seconds

        ---
        Warning: This route has an upgrade available

        ---
        [Diff of the upcoming changes](https://esi.evetech.net/diff/latest/dev/#GET-/characters/{character_id}/fleet/)

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param token str: DESCRIPTION
        :param character_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'token': token}
        path_params = {'character_id': character_id}

        url = f'{self.BASE_URI}/characters/{character_id}/fleet/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_fleets_fleet_id(
        self,
        fleet_id: int,
        datasource: str = 'tranquility',
        token: str = None,
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Return details about a fleet

        ---
        Alternate route: `/dev/fleets/{fleet_id}/`

        Alternate route: `/legacy/fleets/{fleet_id}/`

        Alternate route: `/v1/fleets/{fleet_id}/`

        ---
        This route is cached for up to 5 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param token str: DESCRIPTION
        :param fleet_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'token': token}
        path_params = {'fleet_id': fleet_id}

        url = f'{self.BASE_URI}/fleets/{fleet_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_fleets_fleet_id_members(
        self,
        fleet_id: int,
        datasource: str = 'tranquility',
        language: str = 'en',
        token: str = None,
        accept_language: str = 'en',
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Return information about fleet members

        ---
        Alternate route: `/dev/fleets/{fleet_id}/members/`

        Alternate route: `/legacy/fleets/{fleet_id}/members/`

        Alternate route: `/v1/fleets/{fleet_id}/members/`

        ---
        This route is cached for up to 5 seconds

        :param accept_language str: DESCRIPTION
        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param language str: DESCRIPTION
        :param token str: DESCRIPTION
        :param fleet_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'Accept-Language': accept_language, 'If-None-Match': etag}
        query_params = {'datasource': datasource, 'language': language, 'token': token}
        path_params = {'fleet_id': fleet_id}

        url = f'{self.BASE_URI}/fleets/{fleet_id}/members/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_fleets_fleet_id_wings(
        self,
        fleet_id: int,
        datasource: str = 'tranquility',
        language: str = 'en',
        token: str = None,
        accept_language: str = 'en',
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Return information about wings in a fleet

        ---
        Alternate route: `/dev/fleets/{fleet_id}/wings/`

        Alternate route: `/legacy/fleets/{fleet_id}/wings/`

        Alternate route: `/v1/fleets/{fleet_id}/wings/`

        ---
        This route is cached for up to 5 seconds

        :param accept_language str: DESCRIPTION
        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param language str: DESCRIPTION
        :param token str: DESCRIPTION
        :param fleet_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'Accept-Language': accept_language, 'If-None-Match': etag}
        query_params = {'datasource': datasource, 'language': language, 'token': token}
        path_params = {'fleet_id': fleet_id}

        url = f'{self.BASE_URI}/fleets/{fleet_id}/wings/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)
