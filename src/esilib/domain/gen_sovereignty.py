import json
from typing import List
from esilib.domain.base_domain import BaseDomain
from esilib.exceptions import UnknownAPIStatus
from esilib.models import ESIResponse, ESIResponseMeta


'''
THIS FILE HAS BEEN GENERATED AUTOMATICALLY.
PLEASE DO NOT MODIFY IT DIRECTLY.
'''


class Sovereignty(BaseDomain):
    '''
    ESI API version 1.10.1
    '''
    BASE_PATH = '/latest'

    def get_sovereignty_campaigns(
        self,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Shows sovereignty data for campaigns.

        ---
        Alternate route: `/dev/sovereignty/campaigns/`

        Alternate route: `/legacy/sovereignty/campaigns/`

        Alternate route: `/v1/sovereignty/campaigns/`

        ---
        This route is cached for up to 5 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {}

        url = f'/sovereignty/campaigns/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_sovereignty_map(
        self,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Shows sovereignty information for solar systems

        ---
        Alternate route: `/dev/sovereignty/map/`

        Alternate route: `/legacy/sovereignty/map/`

        Alternate route: `/v1/sovereignty/map/`

        ---
        This route is cached for up to 3600 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {}

        url = f'/sovereignty/map/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_sovereignty_structures(
        self,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Shows sovereignty data for structures.

        ---
        Alternate route: `/dev/sovereignty/structures/`

        Alternate route: `/legacy/sovereignty/structures/`

        Alternate route: `/v1/sovereignty/structures/`

        ---
        This route is cached for up to 120 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {}

        url = f'/sovereignty/structures/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)
