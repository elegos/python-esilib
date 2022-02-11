import json
from typing import List
from esilib.domain.base_domain import BaseDomain
from esilib.exceptions import UnknownAPIStatus
from esilib.models import ESIResponse, ESIResponseMeta


'''
THIS FILE HAS BEEN GENERATED AUTOMATICALLY.
PLEASE DO NOT MODIFY IT DIRECTLY.
'''


class Wars(BaseDomain):
    '''
    ESI API version 1.10.1
    '''
    BASE_PATH = '/latest'

    def get_wars(
        self,
        datasource: str = 'tranquility',
        max_war_id: int = None,
        etag: str = None
    ) -> ESIResponse[List[int]]:
        '''
        Return a list of wars

        ---
        Alternate route: `/dev/wars/`

        Alternate route: `/legacy/wars/`

        Alternate route: `/v1/wars/`

        ---
        This route is cached for up to 3600 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param max_war_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'max_war_id': max_war_id}
        path_params = {}

        url = f'/wars/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_wars_war_id(
        self,
        war_id: int,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Return details about a war

        ---
        Alternate route: `/dev/wars/{war_id}/`

        Alternate route: `/legacy/wars/{war_id}/`

        Alternate route: `/v1/wars/{war_id}/`

        ---
        This route is cached for up to 3600 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param war_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {'war_id': war_id}

        url = f'/wars/{war_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_wars_war_id_killmails(
        self,
        war_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Return a list of kills related to a war

        ---
        Alternate route: `/dev/wars/{war_id}/killmails/`

        Alternate route: `/legacy/wars/{war_id}/killmails/`

        Alternate route: `/v1/wars/{war_id}/killmails/`

        ---
        This route is cached for up to 3600 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param page int: DESCRIPTION
        :param war_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'page': page}
        path_params = {'war_id': war_id}

        url = f'/wars/{war_id}/killmails/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)
