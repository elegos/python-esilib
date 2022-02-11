import json
from typing import List
from esilib.domain.base_domain import BaseDomain
from esilib.exceptions import UnknownAPIStatus
from esilib.models import ESIResponse, ESIResponseMeta


'''
THIS FILE HAS BEEN GENERATED AUTOMATICALLY.
PLEASE DO NOT MODIFY IT DIRECTLY.
'''


class Contracts(BaseDomain):
    '''
    ESI API version 1.10.1
    '''
    BASE_PATH = '/latest'

    def get_characters_character_id_contracts(
        self,
        character_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Returns contracts available to a character, only if the character is issuer, acceptor or assignee. Only returns contracts no older than 30 days, or if the status is "in_progress".

        ---
        Alternate route: `/dev/characters/{character_id}/contracts/`

        Alternate route: `/legacy/characters/{character_id}/contracts/`

        Alternate route: `/v1/characters/{character_id}/contracts/`

        ---
        This route is cached for up to 300 seconds

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

        url = f'/characters/{character_id}/contracts/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_characters_character_id_contracts_contract_id_bids(
        self,
        character_id: int,
        contract_id: int,
        datasource: str = 'tranquility',
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Lists bids on a particular auction contract

        ---
        Alternate route: `/dev/characters/{character_id}/contracts/{contract_id}/bids/`

        Alternate route: `/legacy/characters/{character_id}/contracts/{contract_id}/bids/`

        Alternate route: `/v1/characters/{character_id}/contracts/{contract_id}/bids/`

        ---
        This route is cached for up to 300 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param token str: DESCRIPTION
        :param character_id int: DESCRIPTION
        :param contract_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'token': token}
        path_params = {'character_id': character_id, 'contract_id': contract_id}

        url = f'/characters/{character_id}/contracts/{contract_id}/bids/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_characters_character_id_contracts_contract_id_items(
        self,
        character_id: int,
        contract_id: int,
        datasource: str = 'tranquility',
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Lists items of a particular contract

        ---
        Alternate route: `/dev/characters/{character_id}/contracts/{contract_id}/items/`

        Alternate route: `/legacy/characters/{character_id}/contracts/{contract_id}/items/`

        Alternate route: `/v1/characters/{character_id}/contracts/{contract_id}/items/`

        ---
        This route is cached for up to 3600 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param token str: DESCRIPTION
        :param character_id int: DESCRIPTION
        :param contract_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'token': token}
        path_params = {'character_id': character_id, 'contract_id': contract_id}

        url = f'/characters/{character_id}/contracts/{contract_id}/items/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_contracts_public_bids_contract_id(
        self,
        contract_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Lists bids on a public auction contract

        ---
        Alternate route: `/dev/contracts/public/bids/{contract_id}/`

        Alternate route: `/legacy/contracts/public/bids/{contract_id}/`

        Alternate route: `/v1/contracts/public/bids/{contract_id}/`

        ---
        This route is cached for up to 300 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param page int: DESCRIPTION
        :param contract_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'page': page}
        path_params = {'contract_id': contract_id}

        url = f'/contracts/public/bids/{contract_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_contracts_public_items_contract_id(
        self,
        contract_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Lists items of a public contract

        ---
        Alternate route: `/dev/contracts/public/items/{contract_id}/`

        Alternate route: `/legacy/contracts/public/items/{contract_id}/`

        Alternate route: `/v1/contracts/public/items/{contract_id}/`

        ---
        This route is cached for up to 3600 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param page int: DESCRIPTION
        :param contract_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'page': page}
        path_params = {'contract_id': contract_id}

        url = f'/contracts/public/items/{contract_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_contracts_public_region_id(
        self,
        region_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Returns a paginated list of all public contracts in the given region

        ---
        Alternate route: `/dev/contracts/public/{region_id}/`

        Alternate route: `/legacy/contracts/public/{region_id}/`

        Alternate route: `/v1/contracts/public/{region_id}/`

        ---
        This route is cached for up to 1800 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param page int: DESCRIPTION
        :param region_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'page': page}
        path_params = {'region_id': region_id}

        url = f'/contracts/public/{region_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_contracts(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Returns contracts available to a corporation, only if the corporation is issuer, acceptor or assignee. Only returns contracts no older than 30 days, or if the status is "in_progress".

        ---
        Alternate route: `/dev/corporations/{corporation_id}/contracts/`

        Alternate route: `/legacy/corporations/{corporation_id}/contracts/`

        Alternate route: `/v1/corporations/{corporation_id}/contracts/`

        ---
        This route is cached for up to 300 seconds

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

        url = f'/corporations/{corporation_id}/contracts/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_contracts_contract_id_bids(
        self,
        contract_id: int,
        corporation_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Lists bids on a particular auction contract

        ---
        Alternate route: `/dev/corporations/{corporation_id}/contracts/{contract_id}/bids/`

        Alternate route: `/legacy/corporations/{corporation_id}/contracts/{contract_id}/bids/`

        Alternate route: `/v1/corporations/{corporation_id}/contracts/{contract_id}/bids/`

        ---
        This route is cached for up to 3600 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param page int: DESCRIPTION
        :param token str: DESCRIPTION
        :param contract_id int: DESCRIPTION
        :param corporation_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'page': page, 'token': token}
        path_params = {'contract_id': contract_id, 'corporation_id': corporation_id}

        url = f'/corporations/{corporation_id}/contracts/{contract_id}/bids/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_contracts_contract_id_items(
        self,
        contract_id: int,
        corporation_id: int,
        datasource: str = 'tranquility',
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Lists items of a particular contract

        ---
        Alternate route: `/dev/corporations/{corporation_id}/contracts/{contract_id}/items/`

        Alternate route: `/legacy/corporations/{corporation_id}/contracts/{contract_id}/items/`

        Alternate route: `/v1/corporations/{corporation_id}/contracts/{contract_id}/items/`

        ---
        This route is cached for up to 3600 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param token str: DESCRIPTION
        :param contract_id int: DESCRIPTION
        :param corporation_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'token': token}
        path_params = {'contract_id': contract_id, 'corporation_id': corporation_id}

        url = f'/corporations/{corporation_id}/contracts/{contract_id}/items/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)
