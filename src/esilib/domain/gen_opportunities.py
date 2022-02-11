import json
from typing import List
from esilib.domain.base_domain import BaseDomain
from esilib.exceptions import UnknownAPIStatus
from esilib.models import ESIResponse, ESIResponseMeta


'''
THIS FILE HAS BEEN GENERATED AUTOMATICALLY.
PLEASE DO NOT MODIFY IT DIRECTLY.
'''


class Opportunities(BaseDomain):
    '''
    ESI API version 1.10.1
    '''
    BASE_PATH = '/latest'

    def get_characters_character_id_opportunities(
        self,
        character_id: int,
        datasource: str = 'tranquility',
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Return a list of tasks finished by a character

        ---
        Alternate route: `/dev/characters/{character_id}/opportunities/`

        Alternate route: `/legacy/characters/{character_id}/opportunities/`

        Alternate route: `/v1/characters/{character_id}/opportunities/`

        ---
        This route is cached for up to 3600 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param token str: DESCRIPTION
        :param character_id int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'token': token}
        path_params = {'character_id': character_id}

        url = f'/characters/{character_id}/opportunities/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_opportunities_groups(
        self,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[List[int]]:
        '''
        Return a list of opportunities groups

        ---
        Alternate route: `/dev/opportunities/groups/`

        Alternate route: `/legacy/opportunities/groups/`

        Alternate route: `/v1/opportunities/groups/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {}

        url = f'/opportunities/groups/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_opportunities_groups_group_id(
        self,
        group_id: int,
        datasource: str = 'tranquility',
        language: str = 'en',
        accept_language: str = 'en',
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Return information of an opportunities group

        ---
        Alternate route: `/dev/opportunities/groups/{group_id}/`

        Alternate route: `/legacy/opportunities/groups/{group_id}/`

        Alternate route: `/v1/opportunities/groups/{group_id}/`

        ---
        This route expires daily at 11:05

        :param accept_language str: DESCRIPTION
        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param language str: DESCRIPTION
        :param group_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'Accept-Language': accept_language, 'If-None-Match': etag}
        query_params = {'datasource': datasource, 'language': language}
        path_params = {'group_id': group_id}

        url = f'/opportunities/groups/{group_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_opportunities_tasks(
        self,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[List[int]]:
        '''
        Return a list of opportunities tasks

        ---
        Alternate route: `/dev/opportunities/tasks/`

        Alternate route: `/legacy/opportunities/tasks/`

        Alternate route: `/v1/opportunities/tasks/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {}

        url = f'/opportunities/tasks/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_opportunities_tasks_task_id(
        self,
        task_id: int,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Return information of an opportunities task

        ---
        Alternate route: `/dev/opportunities/tasks/{task_id}/`

        Alternate route: `/legacy/opportunities/tasks/{task_id}/`

        Alternate route: `/v1/opportunities/tasks/{task_id}/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param task_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {'task_id': task_id}

        url = f'/opportunities/tasks/{task_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)
