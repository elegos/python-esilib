import json
from typing import List
from esilib.domain import DataSource
from esilib.domain.base_domain import BaseDomain
from esilib.exceptions import UnknownAPIStatus
from esilib.models import ESIListResult, ESIResponseMeta


class Alliances(BaseDomain):
    BASE_URI = '/alliances'

    def get_alliances(
        self,
        datasource: DataSource = DataSource.TRANQUILITY,
        etag: str = None
    ) -> ESIListResult[int]:
        '''
        List all active player alliances
        https://esi.evetech.net/ui/#/Alliance/get_alliances

        :param esilib.domain.DataSource datasource: The server name you would like data from
        :param str etag: ETag from a previous request

        :raises esilib.exceptions.NotModified: if etag is passed and the content was not changed since the last call

        :raises esilib.exceptions.BadRequest
        :raises esilib.exceptions.ErrorLimited
        :raises esilib.exceptions.InternalServerError
        :raises esilib.exceptions.ServiceUnavailable
        :raises esilib.exceptions.GatewayTimeout
        '''

        headers = {'If-None-Match': etag}
        response = self._get(f'{self.BASE_URI}/',
                             query_params={'datasource': datasource.value}, headers=headers)

        if response.status_code == 200:
            return ESIListResult[int](meta=ESIResponseMeta(response), data=json.loads(response.content))

        raise UnknownAPIStatus(response)
