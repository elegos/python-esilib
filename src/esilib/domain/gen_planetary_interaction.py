import json
from typing import List
from esilib.domain.base_domain import BaseDomain
from esilib.exceptions import UnknownAPIStatus
from esilib.models import ESIResponse, ESIResponseMeta


'''
THIS FILE HAS BEEN GENERATED AUTOMATICALLY.
PLEASE DO NOT MODIFY IT DIRECTLY.
'''


class PlanetaryInteraction(BaseDomain):
    '''
    ESI API version 1.10.1
    '''
    BASE_PATH = '/latest'

    def get_characters_character_id_planets(
        self,
        character_id: int,
        datasource: str = 'tranquility',
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Returns a list of all planetary colonies owned by a character.

        ---
        Alternate route: `/dev/characters/{character_id}/planets/`

        Alternate route: `/legacy/characters/{character_id}/planets/`

        Alternate route: `/v1/characters/{character_id}/planets/`

        ---
        This route is cached for up to 600 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param token str: DESCRIPTION
        :param character_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'token': token}
        path_params = {'character_id': character_id}

        url = f'{self.BASE_URI}/characters/{character_id}/planets/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_characters_character_id_planets_planet_id(
        self,
        character_id: int,
        planet_id: int,
        datasource: str = 'tranquility',
        token: str = None
    ) -> ESIResponse[dict]:
        '''
        Returns full details on the layout of a single planetary colony, including links, pins and routes. Note: Planetary information is only recalculated when the colony is viewed through the client. Information will not update until this criteria is met.

        ---
        Alternate route: `/dev/characters/{character_id}/planets/{planet_id}/`

        Alternate route: `/v3/characters/{character_id}/planets/{planet_id}/`


        :param datasource str: DESCRIPTION
        :param token str: DESCRIPTION
        :param character_id int: DESCRIPTION
        :param planet_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {}
        query_params = {'datasource': datasource, 'token': token}
        path_params = {'character_id': character_id, 'planet_id': planet_id}

        url = f'{self.BASE_URI}/characters/{character_id}/planets/{planet_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_customs_offices(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        List customs offices owned by a corporation

        ---
        Alternate route: `/dev/corporations/{corporation_id}/customs_offices/`

        Alternate route: `/legacy/corporations/{corporation_id}/customs_offices/`

        Alternate route: `/v1/corporations/{corporation_id}/customs_offices/`

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

        url = f'{self.BASE_URI}/corporations/{corporation_id}/customs_offices/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_universe_schematics_schematic_id(
        self,
        schematic_id: int,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Get information on a planetary factory schematic

        ---
        Alternate route: `/dev/universe/schematics/{schematic_id}/`

        Alternate route: `/legacy/universe/schematics/{schematic_id}/`

        Alternate route: `/v1/universe/schematics/{schematic_id}/`

        ---
        This route is cached for up to 3600 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param schematic_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {'schematic_id': schematic_id}

        url = f'{self.BASE_URI}/universe/schematics/{schematic_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)
