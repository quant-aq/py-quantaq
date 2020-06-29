import json
from quantaq.endpoints import (
    Domain, 
    GET, PUT, POST, DELETE
)


class Models(Domain):
    """Initialize the Models group of endpoints.

    :returns: Domain for Models
    :rtype: quantaq.endpoints.Models
    """
    def __init__(self, client) -> None:
        super(Models, self).__init__(client)

    def add(self, **kwargs) -> list:
        """Add a new calibration model for device with sn = serial number.

        :param str sn: The device serial number (required)
        :param str name: The name of the model
        :param str object_name: The object name of the model itself
        :param str training_file: The object name of the training data file
        :param str param: The parameter [co, co2, no, no2, o3, so2, voc, pm1, pm25, pm10]
        :param dict error: Training error information
        :param dict model: Model overview and details
        :param dict calibration: Calibration and training detials

        :returns: Model information
        :rtype: dict
        """
        return self.client.requests("calibration-models/", verb=POST, **kwargs)

    def get(self, **kwargs) -> dict:
        """Return the calibration models for device with sn = serial number.

        :param str sn: The device serial number

        :returns: Model information
        :rtype: list of dict
        """
        sn = kwargs.pop("sn")

        return self.client.requests("calibration-models/" + sn)