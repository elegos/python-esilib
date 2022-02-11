import json
from typing import List
from esilib.domain.base_domain import BaseDomain
from esilib.exceptions import UnknownAPIStatus
from esilib.models import ESIResponse, ESIResponseMeta


'''
THIS FILE HAS BEEN GENERATED AUTOMATICALLY.
PLEASE DO NOT MODIFY IT DIRECTLY.
'''


class FactionWarfare(BaseDomain):
    '''
    ESI API version 1.10.1
    '''
    BASE_PATH = '/latest'

    def get_characters_character_id_fw_stats(
        self,
        character_id: int,
        datasource: str = 'tranquility',
        token: str = None,
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Statistical overview of a character involved in faction warfare

        ---
        Alternate route: `/dev/characters/{character_id}/fw/stats/`

        Alternate route: `/legacy/characters/{character_id}/fw/stats/`

        Alternate route: `/v1/characters/{character_id}/fw/stats/`

        Alternate route: `/v2/characters/{character_id}/fw/stats/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param token str: DESCRIPTION
        :param character_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'token': token}
        path_params = {'character_id': character_id}

        url = f'{self.BASE_URI}/characters/{character_id}/fw/stats/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_fw_stats(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        token: str = None,
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Statistics about a corporation involved in faction warfare

        ---
        Alternate route: `/dev/corporations/{corporation_id}/fw/stats/`

        Alternate route: `/legacy/corporations/{corporation_id}/fw/stats/`

        Alternate route: `/v1/corporations/{corporation_id}/fw/stats/`

        Alternate route: `/v2/corporations/{corporation_id}/fw/stats/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param token str: DESCRIPTION
        :param corporation_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'token': token}
        path_params = {'corporation_id': corporation_id}

        url = f'{self.BASE_URI}/corporations/{corporation_id}/fw/stats/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_fw_leaderboards(
        self,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Top 4 leaderboard of factions for kills and victory points separated by total, last week and yesterday

        ---
        Alternate route: `/dev/fw/leaderboards/`

        Alternate route: `/legacy/fw/leaderboards/`

        Alternate route: `/v1/fw/leaderboards/`

        Alternate route: `/v2/fw/leaderboards/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {}

        url = f'{self.BASE_URI}/fw/leaderboards/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_fw_leaderboards_characters(
        self,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Top 100 leaderboard of pilots for kills and victory points separated by total, last week and yesterday

        ---
        Alternate route: `/dev/fw/leaderboards/characters/`

        Alternate route: `/legacy/fw/leaderboards/characters/`

        Alternate route: `/v1/fw/leaderboards/characters/`

        Alternate route: `/v2/fw/leaderboards/characters/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {}

        url = f'{self.BASE_URI}/fw/leaderboards/characters/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_fw_leaderboards_corporations(
        self,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Top 10 leaderboard of corporations for kills and victory points separated by total, last week and yesterday

        ---
        Alternate route: `/dev/fw/leaderboards/corporations/`

        Alternate route: `/legacy/fw/leaderboards/corporations/`

        Alternate route: `/v1/fw/leaderboards/corporations/`

        Alternate route: `/v2/fw/leaderboards/corporations/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {}

        url = f'{self.BASE_URI}/fw/leaderboards/corporations/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_fw_stats(
        self,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Statistical overviews of factions involved in faction warfare

        ---
        Alternate route: `/dev/fw/stats/`

        Alternate route: `/legacy/fw/stats/`

        Alternate route: `/v1/fw/stats/`

        Alternate route: `/v2/fw/stats/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {}

        url = f'{self.BASE_URI}/fw/stats/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_fw_systems(
        self,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        An overview of the current ownership of faction warfare solar systems

        ---
        Alternate route: `/dev/fw/systems/`

        Alternate route: `/legacy/fw/systems/`

        Alternate route: `/v2/fw/systems/`

        Alternate route: `/v3/fw/systems/`

        ---
        This route is cached for up to 1800 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {}

        url = f'{self.BASE_URI}/fw/systems/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_fw_wars(
        self,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Data about which NPC factions are at war

        ---
        Alternate route: `/dev/fw/wars/`

        Alternate route: `/legacy/fw/wars/`

        Alternate route: `/v1/fw/wars/`

        Alternate route: `/v2/fw/wars/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :returns: List of factions at war
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {}

        url = f'{self.BASE_URI}/fw/wars/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)
