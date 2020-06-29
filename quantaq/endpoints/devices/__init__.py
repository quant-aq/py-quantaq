import json
from quantaq.endpoints import (
    Domain, 
    GET, PUT, POST, DELETE
)

class Devices(Domain):
    """Initialize the Devices group of endpoints.

    :returns: Domain for Devices
    :rtype: quantaq.models.Devices
    """
    def __init__(self, client) -> None:
        super(Devices, self).__init__(client)

    def list(self, **kwargs) -> list:
        """Return all (available) devices.

        :param str limit: Limit the number of results returned
        :param str sort: Sort the results by a specific attribute
        :param str filter: Filter the query
        :param int per_page: Define the number of results to return per page

        :returns: List of devices.
        :rtype: list of dict
        """
        return self.client.requests("devices/", **kwargs)

    def get(self, **kwargs) -> dict:
        """Return device with sn = sn.

        :param str sn: The device serial number

        :returns: Device information
        :rtype: dict
        """
        sn = kwargs.pop("sn")

        return self.client.requests("devices/" + sn)

    def update(self, **kwargs) -> dict:
        """Update the record of a device with sn = sn

        :param str sn: The device serial number
        :param float lat: geo.latitude
        :param float lon: geo.longitude
        :param str city:
        :param str country: The ISO country code
        :param str description:
        :param bool is_outdoors:
        :param bool is_private:
        :param str device_state:
        :param str timezone:

        :returns: Device information
        :rtype: dict
        """
        sn = kwargs.pop("sn")

        return self.client.requests("devices/" + sn, verb=PUT, **kwargs)

    def add(self, **kwargs) -> dict:
        """Add a new device.

        :param str sn: The device serial number
        :param str model:
        :param float lat: geo.latitude
        :param float lon: geo.longitude
        :param str city:
        :param str country:
        :param str description:
        :param bool is_outdoors:
        :param bool is_private:
        :param str device_state:
        :param str timezone:

        :returns: Device information
        :rtype: dict
        """
        return self.client.requests("devices/", verb=POST, **kwargs)

    def drop(self, **kwargs) -> dict:
        """Delete a device.

        :param str sn: The device serial number

        :returns: status
        :rtype: dict
        """
        sn = kwargs.pop("sn")
        return self.client.requests("devices/" + sn, verb=DELETE)