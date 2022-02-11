import json
from typing import List
from esilib.domain.base_domain import BaseDomain
from esilib.exceptions import UnknownAPIStatus
from esilib.models import ESIResponse, ESIResponseMeta


'''
THIS FILE HAS BEEN GENERATED AUTOMATICALLY.
PLEASE DO NOT MODIFY IT DIRECTLY.
'''


class Universe(BaseDomain):
    '''
    ESI API version 1.10.1
    '''
    BASE_PATH = '/latest'

    def get_universe_ancestries(
        self,
        datasource: str = 'tranquility',
        language: str = 'en',
        accept_language: str = 'en',
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Get all character ancestries

        ---
        Alternate route: `/legacy/universe/ancestries/`

        Alternate route: `/v1/universe/ancestries/`

        ---
        This route expires daily at 11:05

        :param accept_language str: DESCRIPTION
        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param language str: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'Accept-Language': accept_language, 'If-None-Match': etag}
        query_params = {'datasource': datasource, 'language': language}
        path_params = {}

        url = f'{self.BASE_URI}/universe/ancestries/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_universe_asteroid_belts_asteroid_belt_id(
        self,
        asteroid_belt_id: int,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Get information on an asteroid belt

        ---
        Alternate route: `/legacy/universe/asteroid_belts/{asteroid_belt_id}/`

        Alternate route: `/v1/universe/asteroid_belts/{asteroid_belt_id}/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param asteroid_belt_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {'asteroid_belt_id': asteroid_belt_id}

        url = f'{self.BASE_URI}/universe/asteroid_belts/{asteroid_belt_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_universe_bloodlines(
        self,
        datasource: str = 'tranquility',
        language: str = 'en',
        accept_language: str = 'en',
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Get a list of bloodlines

        ---
        Alternate route: `/legacy/universe/bloodlines/`

        Alternate route: `/v1/universe/bloodlines/`

        ---
        This route expires daily at 11:05

        :param accept_language str: DESCRIPTION
        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param language str: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'Accept-Language': accept_language, 'If-None-Match': etag}
        query_params = {'datasource': datasource, 'language': language}
        path_params = {}

        url = f'{self.BASE_URI}/universe/bloodlines/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_universe_categories(
        self,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[List[int]]:
        '''
        Get a list of item categories

        ---
        Alternate route: `/legacy/universe/categories/`

        Alternate route: `/v1/universe/categories/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {}

        url = f'{self.BASE_URI}/universe/categories/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_universe_categories_category_id(
        self,
        category_id: int,
        datasource: str = 'tranquility',
        language: str = 'en',
        accept_language: str = 'en',
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Get information of an item category

        ---
        Alternate route: `/legacy/universe/categories/{category_id}/`

        Alternate route: `/v1/universe/categories/{category_id}/`

        ---
        This route expires daily at 11:05

        :param accept_language str: DESCRIPTION
        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param language str: DESCRIPTION
        :param category_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'Accept-Language': accept_language, 'If-None-Match': etag}
        query_params = {'datasource': datasource, 'language': language}
        path_params = {'category_id': category_id}

        url = f'{self.BASE_URI}/universe/categories/{category_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_universe_constellations(
        self,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[List[int]]:
        '''
        Get a list of constellations

        ---
        Alternate route: `/legacy/universe/constellations/`

        Alternate route: `/v1/universe/constellations/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {}

        url = f'{self.BASE_URI}/universe/constellations/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_universe_constellations_constellation_id(
        self,
        constellation_id: int,
        datasource: str = 'tranquility',
        language: str = 'en',
        accept_language: str = 'en',
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Get information on a constellation

        ---
        Alternate route: `/legacy/universe/constellations/{constellation_id}/`

        Alternate route: `/v1/universe/constellations/{constellation_id}/`

        ---
        This route expires daily at 11:05

        :param accept_language str: DESCRIPTION
        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param language str: DESCRIPTION
        :param constellation_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'Accept-Language': accept_language, 'If-None-Match': etag}
        query_params = {'datasource': datasource, 'language': language}
        path_params = {'constellation_id': constellation_id}

        url = f'{self.BASE_URI}/universe/constellations/{constellation_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_universe_factions(
        self,
        datasource: str = 'tranquility',
        language: str = 'en',
        accept_language: str = 'en',
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Get a list of factions

        ---
        Alternate route: `/dev/universe/factions/`

        Alternate route: `/v2/universe/factions/`

        ---
        This route expires daily at 11:05

        :param accept_language str: DESCRIPTION
        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param language str: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'Accept-Language': accept_language, 'If-None-Match': etag}
        query_params = {'datasource': datasource, 'language': language}
        path_params = {}

        url = f'{self.BASE_URI}/universe/factions/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_universe_graphics(
        self,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[List[int]]:
        '''
        Get a list of graphics

        ---
        Alternate route: `/legacy/universe/graphics/`

        Alternate route: `/v1/universe/graphics/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {}

        url = f'{self.BASE_URI}/universe/graphics/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_universe_graphics_graphic_id(
        self,
        graphic_id: int,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Get information on a graphic

        ---
        Alternate route: `/dev/universe/graphics/{graphic_id}/`

        Alternate route: `/legacy/universe/graphics/{graphic_id}/`

        Alternate route: `/v1/universe/graphics/{graphic_id}/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param graphic_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {'graphic_id': graphic_id}

        url = f'{self.BASE_URI}/universe/graphics/{graphic_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_universe_groups(
        self,
        datasource: str = 'tranquility',
        page: int = 1,
        etag: str = None
    ) -> ESIResponse[List[int]]:
        '''
        Get a list of item groups

        ---
        Alternate route: `/legacy/universe/groups/`

        Alternate route: `/v1/universe/groups/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param page int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'page': page}
        path_params = {}

        url = f'{self.BASE_URI}/universe/groups/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_universe_groups_group_id(
        self,
        group_id: int,
        datasource: str = 'tranquility',
        language: str = 'en',
        accept_language: str = 'en',
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Get information on an item group

        ---
        Alternate route: `/dev/universe/groups/{group_id}/`

        Alternate route: `/legacy/universe/groups/{group_id}/`

        Alternate route: `/v1/universe/groups/{group_id}/`

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

        url = f'{self.BASE_URI}/universe/groups/{group_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_universe_moons_moon_id(
        self,
        moon_id: int,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Get information on a moon

        ---
        Alternate route: `/legacy/universe/moons/{moon_id}/`

        Alternate route: `/v1/universe/moons/{moon_id}/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param moon_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {'moon_id': moon_id}

        url = f'{self.BASE_URI}/universe/moons/{moon_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_universe_planets_planet_id(
        self,
        planet_id: int,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Get information on a planet

        ---
        Alternate route: `/legacy/universe/planets/{planet_id}/`

        Alternate route: `/v1/universe/planets/{planet_id}/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param planet_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {'planet_id': planet_id}

        url = f'{self.BASE_URI}/universe/planets/{planet_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_universe_races(
        self,
        datasource: str = 'tranquility',
        language: str = 'en',
        accept_language: str = 'en',
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Get a list of character races

        ---
        Alternate route: `/dev/universe/races/`

        Alternate route: `/legacy/universe/races/`

        Alternate route: `/v1/universe/races/`

        ---
        This route expires daily at 11:05

        :param accept_language str: DESCRIPTION
        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param language str: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'Accept-Language': accept_language, 'If-None-Match': etag}
        query_params = {'datasource': datasource, 'language': language}
        path_params = {}

        url = f'{self.BASE_URI}/universe/races/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_universe_regions(
        self,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[List[int]]:
        '''
        Get a list of regions

        ---
        Alternate route: `/legacy/universe/regions/`

        Alternate route: `/v1/universe/regions/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {}

        url = f'{self.BASE_URI}/universe/regions/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_universe_regions_region_id(
        self,
        region_id: int,
        datasource: str = 'tranquility',
        language: str = 'en',
        accept_language: str = 'en',
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Get information on a region

        ---
        Alternate route: `/legacy/universe/regions/{region_id}/`

        Alternate route: `/v1/universe/regions/{region_id}/`

        ---
        This route expires daily at 11:05

        :param accept_language str: DESCRIPTION
        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param language str: DESCRIPTION
        :param region_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'Accept-Language': accept_language, 'If-None-Match': etag}
        query_params = {'datasource': datasource, 'language': language}
        path_params = {'region_id': region_id}

        url = f'{self.BASE_URI}/universe/regions/{region_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_universe_stargates_stargate_id(
        self,
        stargate_id: int,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Get information on a stargate

        ---
        Alternate route: `/legacy/universe/stargates/{stargate_id}/`

        Alternate route: `/v1/universe/stargates/{stargate_id}/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param stargate_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {'stargate_id': stargate_id}

        url = f'{self.BASE_URI}/universe/stargates/{stargate_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_universe_stars_star_id(
        self,
        star_id: int,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Get information on a star

        ---
        Alternate route: `/legacy/universe/stars/{star_id}/`

        Alternate route: `/v1/universe/stars/{star_id}/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param star_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {'star_id': star_id}

        url = f'{self.BASE_URI}/universe/stars/{star_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_universe_stations_station_id(
        self,
        station_id: int,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Get information on a station

        ---
        Alternate route: `/dev/universe/stations/{station_id}/`

        Alternate route: `/v2/universe/stations/{station_id}/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param station_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {'station_id': station_id}

        url = f'{self.BASE_URI}/universe/stations/{station_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_universe_structures(
        self,
        datasource: str = 'tranquility',
        filter: str = None,
        etag: str = None
    ) -> ESIResponse[List[int]]:
        '''
        List all public structures

        ---
        Alternate route: `/dev/universe/structures/`

        Alternate route: `/legacy/universe/structures/`

        Alternate route: `/v1/universe/structures/`

        ---
        This route is cached for up to 3600 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param filter str: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'filter': filter}
        path_params = {}

        url = f'{self.BASE_URI}/universe/structures/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_universe_structures_structure_id(
        self,
        structure_id: int,
        datasource: str = 'tranquility',
        token: str = None,
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Returns information on requested structure if you are on the ACL. Otherwise, returns "Forbidden" for all inputs.

        ---
        Alternate route: `/v2/universe/structures/{structure_id}/`

        ---
        This route is cached for up to 3600 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param token str: DESCRIPTION
        :param structure_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'token': token}
        path_params = {'structure_id': structure_id}

        url = f'{self.BASE_URI}/universe/structures/{structure_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_universe_system_jumps(
        self,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Get the number of jumps in solar systems within the last hour ending at the timestamp of the Last-Modified header, excluding wormhole space. Only systems with jumps will be listed

        ---
        Alternate route: `/legacy/universe/system_jumps/`

        Alternate route: `/v1/universe/system_jumps/`

        ---
        This route is cached for up to 3600 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {}

        url = f'{self.BASE_URI}/universe/system_jumps/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_universe_system_kills(
        self,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[List[dict]]:
        '''
        Get the number of ship, pod and NPC kills per solar system within the last hour ending at the timestamp of the Last-Modified header, excluding wormhole space. Only systems with kills will be listed

        ---
        Alternate route: `/v2/universe/system_kills/`

        ---
        This route is cached for up to 3600 seconds

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {}

        url = f'{self.BASE_URI}/universe/system_kills/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_universe_systems(
        self,
        datasource: str = 'tranquility',
        etag: str = None
    ) -> ESIResponse[List[int]]:
        '''
        Get a list of solar systems

        ---
        Alternate route: `/dev/universe/systems/`

        Alternate route: `/legacy/universe/systems/`

        Alternate route: `/v1/universe/systems/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource}
        path_params = {}

        url = f'{self.BASE_URI}/universe/systems/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_universe_systems_system_id(
        self,
        system_id: int,
        datasource: str = 'tranquility',
        language: str = 'en',
        accept_language: str = 'en',
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Get information on a solar system.

        ---
        Alternate route: `/dev/universe/systems/{system_id}/`

        Alternate route: `/v4/universe/systems/{system_id}/`

        ---
        This route expires daily at 11:05

        :param accept_language str: DESCRIPTION
        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param language str: DESCRIPTION
        :param system_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'Accept-Language': accept_language, 'If-None-Match': etag}
        query_params = {'datasource': datasource, 'language': language}
        path_params = {'system_id': system_id}

        url = f'{self.BASE_URI}/universe/systems/{system_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_universe_types(
        self,
        datasource: str = 'tranquility',
        page: int = 1,
        etag: str = None
    ) -> ESIResponse[List[int]]:
        '''
        Get a list of type ids

        ---
        Alternate route: `/legacy/universe/types/`

        Alternate route: `/v1/universe/types/`

        ---
        This route expires daily at 11:05

        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param page int: DESCRIPTION
        :returns: 200 ok array
        '''  # nopep8

        header_params = {'If-None-Match': etag}
        query_params = {'datasource': datasource, 'page': page}
        path_params = {}

        url = f'{self.BASE_URI}/universe/types/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)

    def get_universe_types_type_id(
        self,
        type_id: int,
        datasource: str = 'tranquility',
        language: str = 'en',
        accept_language: str = 'en',
        etag: str = None
    ) -> ESIResponse[dict]:
        '''
        Get information on a type

        ---
        Alternate route: `/dev/universe/types/{type_id}/`

        Alternate route: `/v3/universe/types/{type_id}/`

        ---
        This route expires daily at 11:05

        :param accept_language str: DESCRIPTION
        :param etag str: DESCRIPTION
        :param datasource str: DESCRIPTION
        :param language str: DESCRIPTION
        :param type_id int: DESCRIPTION
        :returns: 200 ok object
        '''  # nopep8

        header_params = {'Accept-Language': accept_language, 'If-None-Match': etag}
        query_params = {'datasource': datasource, 'language': language}
        path_params = {'type_id': type_id}

        url = f'{self.BASE_URI}/universe/types/{type_id}/'
        if path_params:
            url = url.format(**path_params)

        response = self._get(url, query_params=query_params, headers=header_params)

        if response.status_code == 200:
            # return type WIP
            return ESIResponse(meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)
