import json
from typing import List
from esilib.domain.base_domain import BaseDomain
from esilib.exceptions import UnknownAPIStatus
from esilib.models import ESIResponse, ESIResponseMeta


'''
THIS FILE HAS BEEN GENERATED AUTOMATICALLY.
PLEASE DO NOT MODIFY IT DIRECTLY.
'''


class Dogma(BaseDomain):
    '''
    ESI API version 1.10.1
    '''
    BASE_PATH = '/latest'

    def get_dogma_attributes(
        self,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[List[int]]:
        '''
        Get a list of dogma attribute ids

        ---
        Alternate route: `/dev/dogma/attributes/`

        Alternate route: `/legacy/dogma/attributes/`

        Alternate route: `/v1/dogma/attributes/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {}

        url = f'{self.BASE_URI}/dogma/attributes/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_dogma_attributes_attribute_id(
        self,
        attribute_id: int,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Get information on a dogma attribute

        ---
        Alternate route: `/dev/dogma/attributes/{attribute_id}/`

        Alternate route: `/legacy/dogma/attributes/{attribute_id}/`

        Alternate route: `/v1/dogma/attributes/{attribute_id}/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param attribute_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {'attribute_id': attribute_id}

        url = f'{self.BASE_URI}/dogma/attributes/{attribute_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_dogma_dynamic_items_type_id_item_id(
        self,
        item_id: int,
        type_id: int,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Returns info about a dynamic item resulting from mutation with a mutaplasmid.

        ---
        Alternate route: `/dev/dogma/dynamic/items/{type_id}/{item_id}/`

        Alternate route: `/legacy/dogma/dynamic/items/{type_id}/{item_id}/`

        Alternate route: `/v1/dogma/dynamic/items/{type_id}/{item_id}/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param item_id int: DESCRIPTION
        :param type_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {'item_id': item_id, 'type_id': type_id}

        url = f'{self.BASE_URI}/dogma/dynamic/items/{type_id}/{item_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_dogma_effects(
        self,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[List[int]]:
        '''
        Get a list of dogma effect ids

        ---
        Alternate route: `/dev/dogma/effects/`

        Alternate route: `/legacy/dogma/effects/`

        Alternate route: `/v1/dogma/effects/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {}

        url = f'{self.BASE_URI}/dogma/effects/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_dogma_effects_effect_id(
        self,
        effect_id: int,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Get information on a dogma effect

        ---
        Alternate route: `/dev/dogma/effects/{effect_id}/`

        Alternate route: `/v2/dogma/effects/{effect_id}/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param effect_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {'effect_id': effect_id}

        url = f'{self.BASE_URI}/dogma/effects/{effect_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)
