import json
from typing import List
from esilib.domain.base_domain import BaseDomain
from esilib.exceptions import UnknownAPIStatus
from esilib.models import ESIResponse, ESIResponseMeta


'''
THIS FILE HAS BEEN GENERATED AUTOMATICALLY.
PLEASE DO NOT MODIFY IT DIRECTLY.
'''


class Killmails(BaseDomain):
    '''
    ESI API version 1.10.1
    '''
    BASE_PATH = '/latest'

    def get_characters_character_id_killmails_recent(
        self,
        character_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Return a list of a character's kills and losses going back 90 days

        ---
        Alternate route: `/dev/characters/{character_id}/killmails/recent/`

        Alternate route: `/legacy/characters/{character_id}/killmails/recent/`

        Alternate route: `/v1/characters/{character_id}/killmails/recent/`

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

        url = f'{self.BASE_URI}/characters/{character_id}/killmails/recent/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_killmails_recent(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Get a list of a corporation's kills and losses going back 90 days

        ---
        Alternate route: `/dev/corporations/{corporation_id}/killmails/recent/`

        Alternate route: `/legacy/corporations/{corporation_id}/killmails/recent/`

        Alternate route: `/v1/corporations/{corporation_id}/killmails/recent/`

        ---
        This route is cached for up to 300 seconds

        ---
        Requires one of the following EVE corporation role(s): Director


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

        url = f'{self.BASE_URI}/corporations/{corporation_id}/killmails/recent/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_killmails_killmail_id_killmail_hash(
        self,
        killmail_hash: str,
        killmail_id: int,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Return a single killmail from its ID and hash

        ---
        Alternate route: `/dev/killmails/{killmail_id}/{killmail_hash}/`

        Alternate route: `/legacy/killmails/{killmail_id}/{killmail_hash}/`

        Alternate route: `/v1/killmails/{killmail_id}/{killmail_hash}/`

        ---
        This route is cached for up to 30758400 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param killmail_hash str: DESCRIPTION
        :param killmail_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {'killmail_hash': killmail_hash, 'killmail_id': killmail_id}

        url = f'{self.BASE_URI}/killmails/{killmail_id}/{killmail_hash}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)
