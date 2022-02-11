import json
from typing import List
from esilib.domain.base_domain import BaseDomain
from esilib.exceptions import UnknownAPIStatus
from esilib.models import ESIResponse, ESIResponseMeta


'''
THIS FILE HAS BEEN GENERATED AUTOMATICALLY.
PLEASE DO NOT MODIFY IT DIRECTLY.
'''


class Insurance(BaseDomain):
    '''
    ESI API version 1.10.1
    '''
    BASE_PATH = '/latest'

    def get_insurance_prices(
        self,
        datasource: str = 'tranquility',
        language: str = 'en',
        accept_language: str = 'en',
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Return available insurance levels for all ship types

        ---
        Alternate route: `/dev/insurance/prices/`

        Alternate route: `/legacy/insurance/prices/`

        Alternate route: `/v1/insurance/prices/`

        ---
        This route is cached for up to 3600 seconds

        :param accept_language str: DESCRIPTION
        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param language str: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'Accept-Language': accept_language, 'If-None-Match': etag}
        query_params = {'datasource': datasource, 'language': language}
        path_params = {}

        url = f'/insurance/prices/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)
