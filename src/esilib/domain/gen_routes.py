import json
from typing import List
from esilib.domain.base_domain import BaseDomain
from esilib.exceptions import UnknownAPIStatus
from esilib.models import ESIResponse, ESIResponseMeta


'''
THIS FILE HAS BEEN GENERATED AUTOMATICALLY.
PLEASE DO NOT MODIFY IT DIRECTLY.
'''


class Routes(BaseDomain):
    '''
    ESI API version 1.10.1
    '''
    BASE_PATH = '/latest'

    def get_route_origin_destination(
        self,
        destination: int,
        origin: int,
        avoid: List[int] = None,
        connections: List[List[int]] = None,
        datasource: str = 'tranquility',
        flag: str = 'shortest',
        etag: str = None
    ) -> ESIResponse[List[int]]:
        '''
        Get the systems between origin and destination

        ---
        Alternate route: `/dev/route/{origin}/{destination}/`

        Alternate route: `/legacy/route/{origin}/{destination}/`

        Alternate route: `/v1/route/{origin}/{destination}/`

        ---
        This route is cached for up to 86400 seconds

        :param etag str: DESCRIPTION
        :param avoid List[int]: DESCRIPTION
        :param connections List[List[int]]: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param flag str: DESCRIPTION
        :param destination int: DESCRIPTION
        :param origin int: DESCRIPTION
        :returns: Solar systems in route
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'avoid': avoid, 'connections': connections,
                        'datasource': datasource, 'flag': flag}
        path_params = {'destination': destination, 'origin': origin}

        url = f'{self.BASE_URI}/route/{origin}/{destination}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)
