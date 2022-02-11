import json
from typing import List
from esilib.domain.base_domain import BaseDomain
from esilib.exceptions import UnknownAPIStatus
from esilib.models import ESIResponse, ESIResponseMeta


'''
THIS FILE HAS BEEN GENERATED AUTOMATICALLY.
PLEASE DO NOT MODIFY IT DIRECTLY.
'''


class Market(BaseDomain):
    '''
    ESI API version 1.10.1
    '''
    BASE_PATH = '/latest'

    def get_characters_character_id_orders(
        self,
        character_id: int,
        datasource: str = 'tranquility',
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        List open market orders placed by a character

        ---
        Alternate route: `/dev/characters/{character_id}/orders/`

        Alternate route: `/v2/characters/{character_id}/orders/`

        ---
        This route is cached for up to 1200 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param token str: DESCRIPTION
        :param character_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'token': token}
        path_params = {'character_id': character_id}

        url = f'/characters/{character_id}/orders/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_characters_character_id_orders_history(
        self,
        character_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        List cancelled and expired market orders placed by a character up to 90 days in the past.

        ---
        Alternate route: `/dev/characters/{character_id}/orders/history/`

        Alternate route: `/legacy/characters/{character_id}/orders/history/`

        Alternate route: `/v1/characters/{character_id}/orders/history/`

        ---
        This route is cached for up to 3600 seconds

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

        url = f'/characters/{character_id}/orders/history/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_orders(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        List open market orders placed on behalf of a corporation

        ---
        Alternate route: `/dev/corporations/{corporation_id}/orders/`

        Alternate route: `/v3/corporations/{corporation_id}/orders/`

        ---
        This route is cached for up to 1200 seconds

        ---
        Requires one of the following EVE corporation role(s): Accountant, Trader


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

        url = f'/corporations/{corporation_id}/orders/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_orders_history(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        List cancelled and expired market orders placed on behalf of a corporation up to 90 days in the past.

        ---
        Alternate route: `/dev/corporations/{corporation_id}/orders/history/`

        Alternate route: `/v2/corporations/{corporation_id}/orders/history/`

        ---
        This route is cached for up to 3600 seconds

        ---
        Requires one of the following EVE corporation role(s): Accountant, Trader


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

        url = f'/corporations/{corporation_id}/orders/history/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_markets_groups(
        self,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[List[int]]:
        '''
        Get a list of item groups

        ---
        Alternate route: `/dev/markets/groups/`

        Alternate route: `/legacy/markets/groups/`

        Alternate route: `/v1/markets/groups/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {}

        url = f'/markets/groups/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_markets_groups_market_group_id(
        self,
        market_group_id: int,
        datasource: str = 'tranquility',
        language: str = 'en',
        accept_language: str = 'en',
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Get information on an item group

        ---
        Alternate route: `/dev/markets/groups/{market_group_id}/`

        Alternate route: `/legacy/markets/groups/{market_group_id}/`

        Alternate route: `/v1/markets/groups/{market_group_id}/`

        ---
        This route expires daily at 11:05

        :param accept_language str: DESCRIPTION
        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param language str: DESCRIPTION
        :param market_group_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'Accept-Language': accept_language, 'If-None-Match': etag}
        query_params = {'datasource': datasource, 'language': language}
        path_params = {'market_group_id': market_group_id}

        url = f'/markets/groups/{market_group_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_markets_prices(
        self,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Return a list of prices

        ---
        Alternate route: `/dev/markets/prices/`

        Alternate route: `/legacy/markets/prices/`

        Alternate route: `/v1/markets/prices/`

        ---
        This route is cached for up to 3600 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {}

        url = f'/markets/prices/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_markets_structures_structure_id(
        self,
        structure_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Return all orders in a structure

        ---
        Alternate route: `/dev/markets/structures/{structure_id}/`

        Alternate route: `/legacy/markets/structures/{structure_id}/`

        Alternate route: `/v1/markets/structures/{structure_id}/`

        ---
        This route is cached for up to 300 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param page int: DESCRIPTION
        :param token str: DESCRIPTION
        :param structure_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'page': page, 'token': token}
        path_params = {'structure_id': structure_id}

        url = f'/markets/structures/{structure_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_markets_region_id_history(
        self,
        region_id: int,
        type_id: int,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Return a list of historical market statistics for the specified type in a region

        ---
        Alternate route: `/dev/markets/{region_id}/history/`

        Alternate route: `/legacy/markets/{region_id}/history/`

        Alternate route: `/v1/markets/{region_id}/history/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param type_id int: DESCRIPTION
        :param region_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'type_id': type_id}
        path_params = {'region_id': region_id}

        url = f'/markets/{region_id}/history/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_markets_region_id_orders(
        self,
        region_id: int,
        order_type: str = 'all',
        datasource: str = 'tranquility',
        page: int = 1,
        type_id: int = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Return a list of orders in a region

        ---
        Alternate route: `/dev/markets/{region_id}/orders/`

        Alternate route: `/legacy/markets/{region_id}/orders/`

        Alternate route: `/v1/markets/{region_id}/orders/`

        ---
        This route is cached for up to 300 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param order_type str: DESCRIPTION
        :param page int: DESCRIPTION
        :param type_id int: DESCRIPTION
        :param region_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource,
                        'order_type': order_type, 'page': page, 'type_id': type_id}
        path_params = {'region_id': region_id}

        url = f'/markets/{region_id}/orders/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_markets_region_id_types(
        self,
        region_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        etag: str = None
    ) -> ESIResponse[List[int]]:
        '''
        Return a list of type IDs that have active orders in the region, for efficient market indexing.

        ---
        Alternate route: `/dev/markets/{region_id}/types/`

        Alternate route: `/legacy/markets/{region_id}/types/`

        Alternate route: `/v1/markets/{region_id}/types/`

        ---
        This route is cached for up to 600 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param page int: DESCRIPTION
        :param region_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'page': page}
        path_params = {'region_id': region_id}

        url = f'/markets/{region_id}/types/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)
