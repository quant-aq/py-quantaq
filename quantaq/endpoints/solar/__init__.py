import json
from quantaq.endpoints import (
    Domain, 
    GET, PUT, POST, DELETE
)


class Solar(Domain):
    """Initialize the Solar group of endpoints.

    :returns: Domain for Solar
    :rtype: quantaq.models.Solar
    """
    def __init__(self, client) -> None:
        super(Solar, self).__init__(client)

    def list(self, **kwargs) -> list:
        """Return all Smart Solar Power System data for device with serial number sn.

        :param str sn: The device serial number
        :param str start: Start date for data retrieval
        :param str stop: End date for data retrieval
        :param str limit: Limit the number of results returned
        :param str sort: Sort the results by a specific attribute
        :param str filter: Filter the query
        :param int per_page: Define the number of results to return per page

        :returns: Data
        :rtype: list of dict
        """
        sn = kwargs.pop("sn")
        endpoint = f"devices/{sn}/data/solar/"

        return self.client.requests(endpoint, **kwargs)