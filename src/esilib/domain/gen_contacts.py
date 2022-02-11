import json
from typing import List
from esilib.domain.base_domain import BaseDomain
from esilib.exceptions import UnknownAPIStatus
from esilib.models import ESIResponse, ESIResponseMeta


'''
THIS FILE HAS BEEN GENERATED AUTOMATICALLY.
PLEASE DO NOT MODIFY IT DIRECTLY.
'''


class Contacts(BaseDomain):
    '''
    ESI API version 1.10.1
    '''
    BASE_PATH = '/latest'

    def get_alliances_alliance_id_contacts(
        self,
        alliance_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Return contacts of an alliance

        ---
        Alternate route: `/dev/alliances/{alliance_id}/contacts/`

        Alternate route: `/v2/alliances/{alliance_id}/contacts/`

        ---
        This route is cached for up to 300 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param page int: DESCRIPTION
        :param token str: DESCRIPTION
        :param alliance_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'page': page, 'token': token}
        path_params = {'alliance_id': alliance_id}

        url = f'{self.BASE_URI}/alliances/{alliance_id}/contacts/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_alliances_alliance_id_contacts_labels(
        self,
        alliance_id: int,
        datasource: str = 'tranquility',
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Return custom labels for an alliance's contacts

        ---
        Alternate route: `/dev/alliances/{alliance_id}/contacts/labels/`

        Alternate route: `/legacy/alliances/{alliance_id}/contacts/labels/`

        Alternate route: `/v1/alliances/{alliance_id}/contacts/labels/`

        ---
        This route is cached for up to 300 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param token str: DESCRIPTION
        :param alliance_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'token': token}
        path_params = {'alliance_id': alliance_id}

        url = f'{self.BASE_URI}/alliances/{alliance_id}/contacts/labels/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_characters_character_id_contacts(
        self,
        character_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Return contacts of a character

        ---
        Alternate route: `/dev/characters/{character_id}/contacts/`

        Alternate route: `/v2/characters/{character_id}/contacts/`

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

        url = f'{self.BASE_URI}/characters/{character_id}/contacts/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_characters_character_id_contacts_labels(
        self,
        character_id: int,
        datasource: str = 'tranquility',
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Return custom labels for a character's contacts

        ---
        Alternate route: `/dev/characters/{character_id}/contacts/labels/`

        Alternate route: `/legacy/characters/{character_id}/contacts/labels/`

        Alternate route: `/v1/characters/{character_id}/contacts/labels/`

        ---
        This route is cached for up to 300 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param token str: DESCRIPTION
        :param character_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'token': token}
        path_params = {'character_id': character_id}

        url = f'{self.BASE_URI}/characters/{character_id}/contacts/labels/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_contacts(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Return contacts of a corporation

        ---
        Alternate route: `/dev/corporations/{corporation_id}/contacts/`

        Alternate route: `/v2/corporations/{corporation_id}/contacts/`

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

        url = f'{self.BASE_URI}/corporations/{corporation_id}/contacts/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_contacts_labels(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Return custom labels for a corporation's contacts

        ---
        Alternate route: `/dev/corporations/{corporation_id}/contacts/labels/`

        Alternate route: `/legacy/corporations/{corporation_id}/contacts/labels/`

        Alternate route: `/v1/corporations/{corporation_id}/contacts/labels/`

        ---
        This route is cached for up to 300 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param token str: DESCRIPTION
        :param corporation_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'token': token}
        path_params = {'corporation_id': corporation_id}

        url = f'{self.BASE_URI}/corporations/{corporation_id}/contacts/labels/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)
