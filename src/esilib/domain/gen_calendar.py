import json
from typing import List
from esilib.domain.base_domain import BaseDomain
from esilib.exceptions import UnknownAPIStatus
from esilib.models import ESIResponse, ESIResponseMeta


'''
THIS FILE HAS BEEN GENERATED AUTOMATICALLY.
PLEASE DO NOT MODIFY IT DIRECTLY.
'''


class Calendar(BaseDomain):
    '''
    ESI API version 1.10.1
    '''
    BASE_PATH = '/latest'

    def get_characters_character_id_calendar(
        self,
        character_id: int,
        datasource: str = 'tranquility',
        from_event: int = None,
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Get 50 event summaries from the calendar. If no from_event ID is given, the resource will return the next 50 chronological event summaries from now. If a from_event ID is specified, it will return the next 50 chronological event summaries from after that event

        ---
        Alternate route: `/dev/characters/{character_id}/calendar/`

        Alternate route: `/legacy/characters/{character_id}/calendar/`

        Alternate route: `/v1/characters/{character_id}/calendar/`

        Alternate route: `/v2/characters/{character_id}/calendar/`

        ---
        This route is cached for up to 5 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param from_event int: DESCRIPTION
        :param token str: DESCRIPTION
        :param character_id int: DESCRIPTION
        :returns: Up to 50 events from now or the event you requested
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'from_event': from_event, 'token': token}
        path_params = {'character_id': character_id}

        url = f'/characters/{character_id}/calendar/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_characters_character_id_calendar_event_id(
        self,
        character_id: int,
        event_id: int,
        datasource: str = 'tranquility',
        token: str = None,
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Get all the information for a specific event

        ---
        Alternate route: `/dev/characters/{character_id}/calendar/{event_id}/`

        Alternate route: `/legacy/characters/{character_id}/calendar/{event_id}/`

        Alternate route: `/v3/characters/{character_id}/calendar/{event_id}/`

        Alternate route: `/v4/characters/{character_id}/calendar/{event_id}/`

        ---
        This route is cached for up to 5 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param token str: DESCRIPTION
        :param character_id int: DESCRIPTION
        :param event_id int: DESCRIPTION
        :returns: Full details of a specific event
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'token': token}
        path_params = {'character_id': character_id, 'event_id': event_id}

        url = f'/characters/{character_id}/calendar/{event_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_characters_character_id_calendar_event_id_attendees(
        self,
        character_id: int,
        event_id: int,
        datasource: str = 'tranquility',
        token: str = None,
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Get all invited attendees for a given event

        ---
        Alternate route: `/dev/characters/{character_id}/calendar/{event_id}/attendees/`

        Alternate route: `/legacy/characters/{character_id}/calendar/{event_id}/attendees/`

        Alternate route: `/v1/characters/{character_id}/calendar/{event_id}/attendees/`

        Alternate route: `/v2/characters/{character_id}/calendar/{event_id}/attendees/`

        ---
        This route is cached for up to 600 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param token str: DESCRIPTION
        :param character_id int: DESCRIPTION
        :param event_id int: DESCRIPTION
        :returns: List of attendees for a given event
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'token': token}
        path_params = {'character_id': character_id, 'event_id': event_id}

        url = f'/characters/{character_id}/calendar/{event_id}/attendees/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)
