import json
from typing import List
from esilib.domain.base_domain import BaseDomain
from esilib.exceptions import UnknownAPIStatus
from esilib.models import ESIResponse, ESIResponseMeta


'''
THIS FILE HAS BEEN GENERATED AUTOMATICALLY.
PLEASE DO NOT MODIFY IT DIRECTLY.
'''


class Wallet(BaseDomain):
    '''
    ESI API version 1.10.1
    '''
    BASE_PATH = '/latest'

    def get_characters_character_id_wallet(
        self,
        character_id: int,
        datasource: str = 'tranquility',
        token: str = None,
        etag: str = None
    ) -> ESIResponse[float]:
        '''
        Returns a character's wallet balance

        ---
        Alternate route: `/legacy/characters/{character_id}/wallet/`

        Alternate route: `/v1/characters/{character_id}/wallet/`

        ---
        This route is cached for up to 120 seconds

        ---
        [Diff of the upcoming changes](https://esi.evetech.net/diff/latest/dev/#GET-/characters/{character_id}/wallet/)

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param token str: DESCRIPTION
        :param character_id int: DESCRIPTION
        :returns: Wallet balance
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'token': token}
        path_params = {'character_id': character_id}

        url = f'{self.BASE_URI}/characters/{character_id}/wallet/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_characters_character_id_wallet_journal(
        self,
        character_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Retrieve the given character's wallet journal going 30 days back

        ---
        Alternate route: `/dev/characters/{character_id}/wallet/journal/`

        Alternate route: `/v6/characters/{character_id}/wallet/journal/`

        ---
        This route is cached for up to 3600 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param page int: DESCRIPTION
        :param token str: DESCRIPTION
        :param character_id int: DESCRIPTION
        :returns: Wallet journal entries
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'page': page, 'token': token}
        path_params = {'character_id': character_id}

        url = f'{self.BASE_URI}/characters/{character_id}/wallet/journal/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_characters_character_id_wallet_transactions(
        self,
        character_id: int,
        datasource: str = 'tranquility',
        from_id: int = None,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Get wallet transactions of a character

        ---
        Alternate route: `/dev/characters/{character_id}/wallet/transactions/`

        Alternate route: `/legacy/characters/{character_id}/wallet/transactions/`

        Alternate route: `/v1/characters/{character_id}/wallet/transactions/`

        ---
        This route is cached for up to 3600 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param from_id int: DESCRIPTION
        :param token str: DESCRIPTION
        :param character_id int: DESCRIPTION
        :returns: Wallet transactions
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'from_id': from_id, 'token': token}
        path_params = {'character_id': character_id}

        url = f'{self.BASE_URI}/characters/{character_id}/wallet/transactions/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_wallets(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Get a corporation's wallets

        ---
        Alternate route: `/dev/corporations/{corporation_id}/wallets/`

        Alternate route: `/legacy/corporations/{corporation_id}/wallets/`

        Alternate route: `/v1/corporations/{corporation_id}/wallets/`

        ---
        This route is cached for up to 300 seconds

        ---
        Requires one of the following EVE corporation role(s): Accountant, Junior_Accountant


        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param token str: DESCRIPTION
        :param corporation_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'token': token}
        path_params = {'corporation_id': corporation_id}

        url = f'{self.BASE_URI}/corporations/{corporation_id}/wallets/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_wallets_division_journal(
        self,
        corporation_id: int,
        division: int,
        datasource: str = 'tranquility',
        page: int = 1,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Retrieve the given corporation's wallet journal for the given division going 30 days back

        ---
        Alternate route: `/dev/corporations/{corporation_id}/wallets/{division}/journal/`

        Alternate route: `/v4/corporations/{corporation_id}/wallets/{division}/journal/`

        ---
        This route is cached for up to 3600 seconds

        ---
        Requires one of the following EVE corporation role(s): Accountant, Junior_Accountant


        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param page int: DESCRIPTION
        :param token str: DESCRIPTION
        :param corporation_id int: DESCRIPTION
        :param division int: DESCRIPTION
        :returns: Journal entries
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'page': page, 'token': token}
        path_params = {'corporation_id': corporation_id, 'division': division}

        url = f'{self.BASE_URI}/corporations/{corporation_id}/wallets/{division}/journal/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_wallets_division_transactions(
        self,
        corporation_id: int,
        division: int,
        datasource: str = 'tranquility',
        from_id: int = None,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Get wallet transactions of a corporation

        ---
        Alternate route: `/dev/corporations/{corporation_id}/wallets/{division}/transactions/`

        Alternate route: `/legacy/corporations/{corporation_id}/wallets/{division}/transactions/`

        Alternate route: `/v1/corporations/{corporation_id}/wallets/{division}/transactions/`

        ---
        This route is cached for up to 3600 seconds

        ---
        Requires one of the following EVE corporation role(s): Accountant, Junior_Accountant


        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param from_id int: DESCRIPTION
        :param token str: DESCRIPTION
        :param corporation_id int: DESCRIPTION
        :param division int: DESCRIPTION
        :returns: Wallet transactions
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'from_id': from_id, 'token': token}
        path_params = {'corporation_id': corporation_id, 'division': division}

        url = f'{self.BASE_URI}/corporations/{corporation_id}/wallets/{division}/transactions/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)
