import json
from typing import List
from esilib.domain.base_domain import BaseDomain
from esilib.exceptions import UnknownAPIStatus
from esilib.models import ESIResponse, ESIResponseMeta


'''
THIS FILE HAS BEEN GENERATED AUTOMATICALLY.
PLEASE DO NOT MODIFY IT DIRECTLY.
'''


class Industry(BaseDomain):
    '''
    ESI API version 1.10.1
    '''
    BASE_PATH = '/latest'

    def get_characters_character_id_industry_jobs(
        self,
        character_id: int,
        datasource: str = 'tranquility',
        include_completed: bool = None,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        List industry jobs placed by a character

        ---
        Alternate route: `/dev/characters/{character_id}/industry/jobs/`

        Alternate route: `/legacy/characters/{character_id}/industry/jobs/`

        Alternate route: `/v1/characters/{character_id}/industry/jobs/`

        ---
        This route is cached for up to 300 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param include_completed bool: DESCRIPTION
        :param token str: DESCRIPTION
        :param character_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource,
                        'include_completed': include_completed, 'token': token}
        path_params = {'character_id': character_id}

        url = f'{self.BASE_URI}/characters/{character_id}/industry/jobs/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_characters_character_id_mining(
        self,
        character_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Paginated record of all mining done by a character for the past 30 days


        ---
        Alternate route: `/dev/characters/{character_id}/mining/`

        Alternate route: `/legacy/characters/{character_id}/mining/`

        Alternate route: `/v1/characters/{character_id}/mining/`

        ---
        This route is cached for up to 600 seconds

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

        url = f'{self.BASE_URI}/characters/{character_id}/mining/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporation_corporation_id_mining_extractions(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Extraction timers for all moon chunks being extracted by refineries belonging to a corporation.


        ---
        Alternate route: `/dev/corporation/{corporation_id}/mining/extractions/`

        Alternate route: `/legacy/corporation/{corporation_id}/mining/extractions/`

        Alternate route: `/v1/corporation/{corporation_id}/mining/extractions/`

        ---
        This route is cached for up to 1800 seconds

        ---
        Requires one of the following EVE corporation role(s): Station_Manager


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

        url = f'{self.BASE_URI}/corporation/{corporation_id}/mining/extractions/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporation_corporation_id_mining_observers(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Paginated list of all entities capable of observing and recording mining for a corporation


        ---
        Alternate route: `/dev/corporation/{corporation_id}/mining/observers/`

        Alternate route: `/legacy/corporation/{corporation_id}/mining/observers/`

        Alternate route: `/v1/corporation/{corporation_id}/mining/observers/`

        ---
        This route is cached for up to 3600 seconds

        ---
        Requires one of the following EVE corporation role(s): Accountant


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

        url = f'{self.BASE_URI}/corporation/{corporation_id}/mining/observers/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporation_corporation_id_mining_observers_observer_id(
        self,
        corporation_id: int,
        observer_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Paginated record of all mining seen by an observer


        ---
        Alternate route: `/dev/corporation/{corporation_id}/mining/observers/{observer_id}/`

        Alternate route: `/legacy/corporation/{corporation_id}/mining/observers/{observer_id}/`

        Alternate route: `/v1/corporation/{corporation_id}/mining/observers/{observer_id}/`

        ---
        This route is cached for up to 3600 seconds

        ---
        Requires one of the following EVE corporation role(s): Accountant


        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param page int: DESCRIPTION
        :param token str: DESCRIPTION
        :param corporation_id int: DESCRIPTION
        :param observer_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'page': page, 'token': token}
        path_params = {'corporation_id': corporation_id, 'observer_id': observer_id}

        url = f'{self.BASE_URI}/corporation/{corporation_id}/mining/observers/{observer_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_industry_jobs(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        include_completed: bool = None,
        page: int = 1,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        List industry jobs run by a corporation

        ---
        Alternate route: `/dev/corporations/{corporation_id}/industry/jobs/`

        Alternate route: `/legacy/corporations/{corporation_id}/industry/jobs/`

        Alternate route: `/v1/corporations/{corporation_id}/industry/jobs/`

        ---
        This route is cached for up to 300 seconds

        ---
        Requires one of the following EVE corporation role(s): Factory_Manager


        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param include_completed bool: DESCRIPTION
        :param page int: DESCRIPTION
        :param token str: DESCRIPTION
        :param corporation_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource,
                        'include_completed': include_completed, 'page': page, 'token': token}
        path_params = {'corporation_id': corporation_id}

        url = f'{self.BASE_URI}/corporations/{corporation_id}/industry/jobs/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_industry_facilities(
        self,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Return a list of industry facilities

        ---
        Alternate route: `/dev/industry/facilities/`

        Alternate route: `/legacy/industry/facilities/`

        Alternate route: `/v1/industry/facilities/`

        ---
        This route is cached for up to 3600 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {}

        url = f'{self.BASE_URI}/industry/facilities/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_industry_systems(
        self,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Return cost indices for solar systems

        ---
        Alternate route: `/dev/industry/systems/`

        Alternate route: `/legacy/industry/systems/`

        Alternate route: `/v1/industry/systems/`

        ---
        This route is cached for up to 3600 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {}

        url = f'{self.BASE_URI}/industry/systems/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)
