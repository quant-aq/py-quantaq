import json
from quantaq.endpoints import (
    Domain, 
    GET, PUT, POST, DELETE
)


class Cellular(Domain):
    """Initialize the Cellular logs group of endpoints.

    :returns: Domain for Cellular
    :rtype: quantaq.endpoints.Cellular
    """
    def __init__(self, client) -> None:
        super(Cellular, self).__init__(client)

    def list(self, **kwargs) -> list:
        """Return a list of cellular logs for a device with 
        serial number sn.

        :param str sn: The device serial number
        :param str start: Start date for log retrieval
        :param str stop: End date for log retrieval
        :param str limit: Limit the number of results returned
        :param str sort: Sort the results by a specific attribute
        :param str filter: Filter the query
        :param int per_page: Define the number of results to return per page

        :returns: Cellular Logs
        :rtype: list of dict
        """
        sn = kwargs.pop("sn")

        return self.client.requests("meta-data/cell-data/{}/".format(sn), **kwargs)
    
    def drop(self, **kwargs) -> dict:
        """Delete a cellular log record.

        :param int id: The id of the cellular log record

        :returns: Status of deletion
        :rtype: dict
        """
        id = kwargs.pop("id")

        return self.client.requests("meta-data/cell-data/" + str(id), verb=DELETE)