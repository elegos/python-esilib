import json
from typing import List
from esilib.domain.base_domain import BaseDomain
from esilib.exceptions import UnknownAPIStatus
from esilib.models import ESIResponse, ESIResponseMeta


'''
THIS FILE HAS BEEN GENERATED AUTOMATICALLY.
PLEASE DO NOT MODIFY IT DIRECTLY.
'''


class Corporation(BaseDomain):
    '''
    ESI API version 1.10.1
    '''
    BASE_PATH = '/latest'

    def get_corporations_npccorps(
        self,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[List[int]]:
        '''
        Get a list of npc corporations

        ---
        Alternate route: `/dev/corporations/npccorps/`

        Alternate route: `/v2/corporations/npccorps/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {}

        url = f'/corporations/npccorps/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Public information about a corporation

        ---
        Alternate route: `/dev/corporations/{corporation_id}/`

        Alternate route: `/v5/corporations/{corporation_id}/`

        ---
        This route is cached for up to 3600 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param corporation_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {'corporation_id': corporation_id}

        url = f'/corporations/{corporation_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_alliancehistory(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Get a list of all the alliances a corporation has been a member of

        ---
        Alternate route: `/dev/corporations/{corporation_id}/alliancehistory/`

        Alternate route: `/v3/corporations/{corporation_id}/alliancehistory/`

        ---
        This route is cached for up to 3600 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param corporation_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {'corporation_id': corporation_id}

        url = f'/corporations/{corporation_id}/alliancehistory/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_blueprints(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Returns a list of blueprints the corporation owns

        ---
        Alternate route: `/dev/corporations/{corporation_id}/blueprints/`

        Alternate route: `/v3/corporations/{corporation_id}/blueprints/`

        ---
        This route is cached for up to 3600 seconds

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

        url = f'/corporations/{corporation_id}/blueprints/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_containers_logs(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Returns logs recorded in the past seven days from all audit log secure containers (ALSC) owned by a given corporation

        ---
        Alternate route: `/dev/corporations/{corporation_id}/containers/logs/`

        Alternate route: `/v3/corporations/{corporation_id}/containers/logs/`

        ---
        This route is cached for up to 600 seconds

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

        url = f'/corporations/{corporation_id}/containers/logs/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_divisions(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        token: str = None,
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Return corporation hangar and wallet division names, only show if a division is not using the default name

        ---
        Alternate route: `/dev/corporations/{corporation_id}/divisions/`

        Alternate route: `/v2/corporations/{corporation_id}/divisions/`

        ---
        This route is cached for up to 3600 seconds

        ---
        Requires one of the following EVE corporation role(s): Director


        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param token str: DESCRIPTION
        :param corporation_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'token': token}
        path_params = {'corporation_id': corporation_id}

        url = f'/corporations/{corporation_id}/divisions/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_facilities(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Return a corporation's facilities

        ---
        Alternate route: `/dev/corporations/{corporation_id}/facilities/`

        Alternate route: `/v2/corporations/{corporation_id}/facilities/`

        ---
        This route is cached for up to 3600 seconds

        ---
        Requires one of the following EVE corporation role(s): Factory_Manager


        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param token str: DESCRIPTION
        :param corporation_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'token': token}
        path_params = {'corporation_id': corporation_id}

        url = f'/corporations/{corporation_id}/facilities/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_icons(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Get the icon urls for a corporation

        ---
        Alternate route: `/dev/corporations/{corporation_id}/icons/`

        Alternate route: `/v2/corporations/{corporation_id}/icons/`

        ---
        This route is cached for up to 3600 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param corporation_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {'corporation_id': corporation_id}

        url = f'/corporations/{corporation_id}/icons/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_medals(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Returns a corporation's medals

        ---
        Alternate route: `/dev/corporations/{corporation_id}/medals/`

        Alternate route: `/v2/corporations/{corporation_id}/medals/`

        ---
        This route is cached for up to 3600 seconds

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

        url = f'/corporations/{corporation_id}/medals/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_medals_issued(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Returns medals issued by a corporation

        ---
        Alternate route: `/dev/corporations/{corporation_id}/medals/issued/`

        Alternate route: `/v2/corporations/{corporation_id}/medals/issued/`

        ---
        This route is cached for up to 3600 seconds

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

        url = f'/corporations/{corporation_id}/medals/issued/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_members(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[int]]:
        '''
        Return the current member list of a corporation, the token's character need to be a member of the corporation.

        ---
        Alternate route: `/dev/corporations/{corporation_id}/members/`

        Alternate route: `/v4/corporations/{corporation_id}/members/`

        ---
        This route is cached for up to 3600 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param token str: DESCRIPTION
        :param corporation_id int: DESCRIPTION
        :returns: A list of character IDs
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'token': token}
        path_params = {'corporation_id': corporation_id}

        url = f'/corporations/{corporation_id}/members/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_members_limit(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        token: str = None,
        etag: str = None
    ) -> ESIResponse[int]:
        '''
        Return a corporation's member limit, not including CEO himself

        ---
        Alternate route: `/dev/corporations/{corporation_id}/members/limit/`

        Alternate route: `/v2/corporations/{corporation_id}/members/limit/`

        ---
        This route is cached for up to 3600 seconds

        ---
        Requires one of the following EVE corporation role(s): Director


        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param token str: DESCRIPTION
        :param corporation_id int: DESCRIPTION
        :returns: 200 ok integer
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'token': token}
        path_params = {'corporation_id': corporation_id}

        url = f'/corporations/{corporation_id}/members/limit/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_members_titles(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Returns a corporation's members' titles

        ---
        Alternate route: `/dev/corporations/{corporation_id}/members/titles/`

        Alternate route: `/v2/corporations/{corporation_id}/members/titles/`

        ---
        This route is cached for up to 3600 seconds

        ---
        Requires one of the following EVE corporation role(s): Director


        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param token str: DESCRIPTION
        :param corporation_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'token': token}
        path_params = {'corporation_id': corporation_id}

        url = f'/corporations/{corporation_id}/members/titles/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_membertracking(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Returns additional information about a corporation's members which helps tracking their activities

        ---
        Alternate route: `/dev/corporations/{corporation_id}/membertracking/`

        Alternate route: `/v2/corporations/{corporation_id}/membertracking/`

        ---
        This route is cached for up to 3600 seconds

        ---
        Requires one of the following EVE corporation role(s): Director


        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param token str: DESCRIPTION
        :param corporation_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'token': token}
        path_params = {'corporation_id': corporation_id}

        url = f'/corporations/{corporation_id}/membertracking/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_roles(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Return the roles of all members if the character has the personnel manager role or any grantable role.

        ---
        Alternate route: `/dev/corporations/{corporation_id}/roles/`

        Alternate route: `/v2/corporations/{corporation_id}/roles/`

        ---
        This route is cached for up to 3600 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param token str: DESCRIPTION
        :param corporation_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'token': token}
        path_params = {'corporation_id': corporation_id}

        url = f'/corporations/{corporation_id}/roles/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_roles_history(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Return how roles have changed for a coporation's members, up to a month

        ---
        Alternate route: `/dev/corporations/{corporation_id}/roles/history/`

        Alternate route: `/v2/corporations/{corporation_id}/roles/history/`

        ---
        This route is cached for up to 3600 seconds

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

        url = f'/corporations/{corporation_id}/roles/history/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_shareholders(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Return the current shareholders of a corporation.

        ---
        Alternate route: `/dev/corporations/{corporation_id}/shareholders/`

        Alternate route: `/legacy/corporations/{corporation_id}/shareholders/`

        Alternate route: `/v1/corporations/{corporation_id}/shareholders/`

        ---
        This route is cached for up to 3600 seconds

        ---
        Requires one of the following EVE corporation role(s): Director


        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param page int: DESCRIPTION
        :param token str: DESCRIPTION
        :param corporation_id int: DESCRIPTION
        :returns: List of shareholders
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'page': page, 'token': token}
        path_params = {'corporation_id': corporation_id}

        url = f'/corporations/{corporation_id}/shareholders/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_standings(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Return corporation standings from agents, NPC corporations, and factions

        ---
        Alternate route: `/dev/corporations/{corporation_id}/standings/`

        Alternate route: `/v2/corporations/{corporation_id}/standings/`

        ---
        This route is cached for up to 3600 seconds

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

        url = f'/corporations/{corporation_id}/standings/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_starbases(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        page: int = 1,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Returns list of corporation starbases (POSes)

        ---
        Alternate route: `/dev/corporations/{corporation_id}/starbases/`

        Alternate route: `/v2/corporations/{corporation_id}/starbases/`

        ---
        This route is cached for up to 3600 seconds

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

        url = f'/corporations/{corporation_id}/starbases/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_starbases_starbase_id(
        self,
        corporation_id: int,
        starbase_id: int,
        system_id: int,
        datasource: str = 'tranquility',
        token: str = None,
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Returns various settings and fuels of a starbase (POS)

        ---
        Alternate route: `/dev/corporations/{corporation_id}/starbases/{starbase_id}/`

        Alternate route: `/v2/corporations/{corporation_id}/starbases/{starbase_id}/`

        ---
        This route is cached for up to 3600 seconds

        ---
        Requires one of the following EVE corporation role(s): Director


        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param system_id int: DESCRIPTION
        :param token str: DESCRIPTION
        :param corporation_id int: DESCRIPTION
        :param starbase_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'system_id': system_id, 'token': token}
        path_params = {'corporation_id': corporation_id, 'starbase_id': starbase_id}

        url = f'/corporations/{corporation_id}/starbases/{starbase_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_structures(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        language: str = 'en',
        page: int = 1,
        token: str = None,
        accept_language: str = 'en',
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Get a list of corporation structures. This route's version includes the changes to structures detailed in this blog: https://www.eveonline.com/article/upwell-2.0-structures-changes-coming-on-february-13th

        ---
        Alternate route: `/dev/corporations/{corporation_id}/structures/`

        Alternate route: `/v4/corporations/{corporation_id}/structures/`

        ---
        This route is cached for up to 3600 seconds

        ---
        Requires one of the following EVE corporation role(s): Station_Manager


        :param accept_language str: DESCRIPTION
        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param language str: DESCRIPTION
        :param page int: DESCRIPTION
        :param token str: DESCRIPTION
        :param corporation_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'Accept-Language': accept_language, 'If-None-Match': etag}
        query_params = {'datasource': datasource,
                        'language': language, 'page': page, 'token': token}
        path_params = {'corporation_id': corporation_id}

        url = f'/corporations/{corporation_id}/structures/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_corporations_corporation_id_titles(
        self,
        corporation_id: int,
        datasource: str = 'tranquility',
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Returns a corporation's titles

        ---
        Alternate route: `/dev/corporations/{corporation_id}/titles/`

        Alternate route: `/v2/corporations/{corporation_id}/titles/`

        ---
        This route is cached for up to 3600 seconds

        ---
        Requires one of the following EVE corporation role(s): Director


        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param token str: DESCRIPTION
        :param corporation_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'token': token}
        path_params = {'corporation_id': corporation_id}

        url = f'/corporations/{corporation_id}/titles/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)
