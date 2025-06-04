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

    def bydate(self, **kwargs) -> list:
        """Return all data for a device with serial number <sn> 
        on date <date>.

        :param str sn: The device serial number
        :param str date: The date to retrieve data for in YYYY-MM-DD format (all GMT).
        :param bool raw: Return the raw (not final), default is False

        :returns: Data
        :rtype: list of dicts
        """
        sn = kwargs.pop("sn")
        date = kwargs.pop("date")
        raw = kwargs.pop("raw", False)

        endpoint = "devices/" + sn + "/data-by-date/"
        if raw:
            endpoint += "raw/"
        
        endpoint += date + "/"

        return self.client.requests(endpoint)
    
    def byinterval(self, **kwargs) -> list:
        """Return resampled data for a device with serial number <sn> between <start_date> 
        and <end_date> using resample period <period>.

        :param str sn: The device serial number
        :param str start_date: The start date to retrieve data for in YYYY-MM-DD format (all GMT)
        :param str end_date: The end date to retrieve data for in YYYY-MM-DD format (all GMT)
        :param str period: The resample period; one of ['15min', '1h', '8h', or '1d']
        
        :returns: paginated list of resampled data
        :rtype: list of dicts
        
        """
        sn = kwargs.pop("sn")
        start = kwargs.pop("start_date")
        end = kwargs.pop("end_date")
        period = kwargs.pop("period")
        
        endpoint = f"devices/{sn}/data/resampled/?start_date={start}&end_date={end}&period={period}"
        
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
