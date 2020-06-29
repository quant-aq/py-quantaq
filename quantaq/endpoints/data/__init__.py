import json
from quantaq.endpoints import (
    Domain, 
    GET, PUT, POST, DELETE
)


class Data(Domain):
    """Initialize the Data group of endpoints.

    :returns: Domain for Data
    :rtype: quantaq.models.Data
    """
    def __init__(self, client) -> None:
        super(Data, self).__init__(client)

    def list(self, **kwargs) -> list:
        """Return all data for device with serial number sn.

        :param str sn: The device serial number
        :param bool raw: Return the raw (not final), default is False
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
        raw = kwargs.pop("raw", False)
        endpoint = "devices/" + sn + "/data/"
        
        if raw:
            endpoint += "raw/"

        return self.client.requests(endpoint, **kwargs)

    def get(self, **kwargs) -> dict:
        """Return a single data point.

        :param str sn: The device serial number
        :param int id: The id of the data point
        :param bool raw: Return the raw (not final), default is False

        :returns: Data information
        :rtype: dict
        """
        sn = kwargs.pop("sn")
        id = kwargs.pop("id")
        raw = kwargs.pop("raw", False)

        endpoint = "devices/" + sn + '/data/'
        if raw:
            endpoint += "raw/"
        endpoint += str(id)

        return self.client.requests(endpoint)
