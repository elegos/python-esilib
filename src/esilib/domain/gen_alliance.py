import json
from typing import List
from esilib.domain.base_domain import BaseDomain
from esilib.exceptions import UnknownAPIStatus
from esilib.models import ESIResponse, ESIResponseMeta


'''
THIS FILE HAS BEEN GENERATED AUTOMATICALLY.
PLEASE DO NOT MODIFY IT DIRECTLY.
'''


class Alliance(BaseDomain):
    '''
    ESI API version 1.10.1
    '''
    BASE_PATH = '/latest'

    def get_alliances(
        self,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[List[int]]:
        '''
        List all active player alliances

        ---
        Alternate route: `/dev/alliances/`

        Alternate route: `/legacy/alliances/`

        Alternate route: `/v1/alliances/`

        Alternate route: `/v2/alliances/`

        ---
        This route is cached for up to 3600 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {}

        url = f'/alliances/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_alliances_alliance_id(
        self,
        alliance_id: int,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Public information about an alliance

        ---
        Alternate route: `/dev/alliances/{alliance_id}/`

        Alternate route: `/legacy/alliances/{alliance_id}/`

        Alternate route: `/v3/alliances/{alliance_id}/`

        Alternate route: `/v4/alliances/{alliance_id}/`

        ---
        This route is cached for up to 3600 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param alliance_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {'alliance_id': alliance_id}

        url = f'/alliances/{alliance_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_alliances_alliance_id_corporations(
        self,
        alliance_id: int,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[List[int]]:
        '''
        List all current member corporations of an alliance

        ---
        Alternate route: `/dev/alliances/{alliance_id}/corporations/`

        Alternate route: `/legacy/alliances/{alliance_id}/corporations/`

        Alternate route: `/v1/alliances/{alliance_id}/corporations/`

        Alternate route: `/v2/alliances/{alliance_id}/corporations/`

        ---
        This route is cached for up to 3600 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param alliance_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {'alliance_id': alliance_id}

        url = f'/alliances/{alliance_id}/corporations/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_alliances_alliance_id_icons(
        self,
        alliance_id: int,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Get the icon urls for a alliance

        ---
        Alternate route: `/legacy/alliances/{alliance_id}/icons/`

        Alternate route: `/v1/alliances/{alliance_id}/icons/`

        ---
        This route expires daily at 11:05

        ---
        [Diff of the upcoming changes](https://esi.evetech.net/diff/latest/dev/#GET-/alliances/{alliance_id}/icons/)

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param alliance_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {'alliance_id': alliance_id}

        url = f'/alliances/{alliance_id}/icons/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)
