import json
from quantaq.endpoints import (
    Domain, 
    GET, PUT, POST, DELETE
)


class Logs(Domain):
    """Initialize the Logs group of endpoints.

    :returns: Domain for Logs
    :rtype: quantaq.models.Logs
    """
    def __init__(self, client) -> None:
        super(Logs, self).__init__(client)

    def list(self, **kwargs) -> list:
        """Return a list of logs for device with serial number sn.

        :param str sn: The device serial number
        :param str start: Start date for log retrieval
        :param str stop: End date for log retrieval
        :param str limit: Limit the number of results returned
        :param str sort: Sort the results by a specific attribute
        :param str filter: Filter the query
        :param int per_page: Define the number of results to return per page

        :returns: Logs
        :rtype: list of dict
        """
        sn = kwargs.pop("sn")

        return self.client.requests("log/{}/".format(sn), **kwargs)

    def get(self, **kwargs) -> dict:
        """Return a single log.

        :param int id: The id of the log

        :returns: Log information
        :rtype: dict
        """
        id = kwargs.pop("id")

        return self.client.requests("log/" + str(id))

    def update(self, **kwargs) -> dict:
        """Update a log record.

        :param int id: The log id
        :param str level: One of ['INFO', 'WARNING', 'CRITICAL']
        :param str message: The log message

        :returns: Log information
        :rtype: dict
        """
        id = kwargs.pop("id")

        return self.client.requests("log/" + str(id), verb=PUT, **kwargs)
    
    def drop(self, **kwargs) -> dict:
        """Delete the log record.

        :param int id: The log id

        :returns: API call status
        :rytpe: dict
        """
        id = kwargs.pop("id")

        return self.client.requests("log/" + str(id), verb=DELETE)