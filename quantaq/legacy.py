# -*- coding: utf-8 -*-
from .baseapi import BaseAPI, PUT, DELETE, POST, GET
from .baseapi import BaseAPI
from .utils import list_to_dataframe

class QuantAQ(BaseAPI):
    def __init__(self, *args, **kwargs):
        super(QuantAQ, self).__init__(*args, **kwargs)
    
    def get_account(self):
        """Return the account information associated with the API key being used.

        Examples
        --------

        >>> api = quantaq.legacy.QuantAQ()
        >>> api.get_account()

        """
        return self.fetch_data("account")
    
    def get_devices(self, return_type="json", **kwargs):
        """Return a list of devices.

        Parameters
        ----------
        return_type: string, required
            Return a list of json objects if set to 'json', or a dataframe if set to 'dataframe'
        params: dict, optional
            Query based on any column or parameter - see utils for further discussion.

        Returns
        -------
        list or dataframe

        Examples
        --------

        Get a list of all devices:

        >>> api = quantaq.legacy.QuantAQ()
        >>> api.get_devices()

        Get a list of all devices as a dataframe:

        >>> api.get_devices(return_type='dataframe')

        Get a list of all devices, but limit to just 2 devices:

        >>> api.get_devices(params=dict(limit=2))

        """
        assert(return_type in ("json", "dataframe")), "Bad return_type"

        data = self.fetch_data("devices/", **kwargs)
        if return_type == "dataframe":
            data = list_to_dataframe(data)
        return data

    def get_device(self, sn):
        """Return a single device.

        Examples
        --------

        >>> api = quantaq.legacy.QuantAQ()
        >>> api.get_device(sn="SN001")

        """
        return self.fetch_data("devices/{}".format(sn))
    
    def update_device(self, sn, **kwargs):
        """Update a device.

        Parameters
        ----------
        sn: string, required
            The device SN
        params: dict, required
            A dictionary containing the information to update.

        Returns
        -------
        device: dict
            A dictionary containing the device data
        
        Examples
        --------

        >>> api = quantaq.legacy.QuantAQ()
        >>> api.update_device(sn="SN001", params=dict(city="cambridge"))
        """
        return self.fetch_data("devices/{}".format(sn), type=PUT, **kwargs)
    
    def delete_device(self, sn):
        """Delete a device.

        Parameters
        ----------
        sn: string, required
            The device SN
        
        Examples
        --------

        >>> api = quantaq.legacy.QuantAQ()
        >>> api.delete_device(sn="SN001")

        """
        return self.fetch_data("devices/{}".format(sn), type=DELETE)

    def add_device(self, **kwargs):
        """Add a new device.

        Parameters
        ----------
        params: dict, required
            A dictionary containing all relevant information including the `sn` and `model`.

        Returns
        -------
        device: dict
            A dictionary containing the device data

        Examples
        --------
        >>> api = quantaq.legacy.QuantAQ()
        >>> api.add_device(params=dict(sn="SN000-001", model="arisense_v200", city="cambridge"))

        """
        return self._make_request("devices/", type=POST, **kwargs)

    def add_data(self, **kwargs):
        """Add new data.

        Parameters
        ----------

        Returns
        -------

        Examples
        --------

        """
        raise NotImplementedError("This method is not yet implemented.")

    def update_data(self, sn, id, **kwargs):
        """Update a data record. This only updates the raw data records.

        Parameters
        ----------
        sn: string, required
            The device SN
        id: int, required
            The id of the individual data point.
        params: dict, required
            A dictionary containing the information to update.

        Returns
        -------
        data: dict
            A dictionary containing the data for a given point.

        Examples
        --------
        >>> api = quantaq.legacy.QuantAQ()
        >>> api.update_data(sn="SN000-001", id=2121, params=dict(lat=43.1))

        """
        return self.fetch_data("devices/{}/data/raw/{}".format(sn, id), type=PUT, **kwargs)
    
    def delete_data(self, sn, id, **kwargs):
        """Delete a data point.

        Parameters
        ----------
        sn: string, required
            The device SN
        id: int, required
            The id of the individual data point.

        Returns
        -------
        success: dict
            A dictionary containing the success or failure of the request.

        Examples
        --------

        """
        return self.fetch_data("devices/{}/data/raw/{}".format(sn, id), type=DELETE)

    def get_data(self, sn, return_type="json", final_data=True, id=None, **kwargs):
        """Return a list of data for a given device.

        Parameters
        ----------
        sn: string, required
            The device SN you would like data for
        return_type: string, required
            Return a list of json objects if set to 'json', or a dataframe if set to 'dataframe'
        final_data: bool
            If True, return the cleand/final data; if False, return the raw data (requires necessary permissions)
        id: int
            You can retrieve an individual data point by its ID.
        params: dict, optional
            Query based on any column or parameter - see utils for further discussion.

        Returns
        -------
        list or dataframe

        Examples
        --------

        >>> api.get_data(sn='<sn>', params=dict(limit=25))

        """
        assert(return_type in ("json", "dataframe")), "Bad return_type"
        endpoint = "devices/{}/data/".format(sn)
        if not final_data:
            endpoint += "raw/"

        if id is not None:
            return self.fetch_data(endpoint + str(id), **kwargs)

        data = self.fetch_data(endpoint, **kwargs)
        if return_type == "dataframe":
            data = list_to_dataframe(data)
        return data

    def get_logs(self, sn, return_type="json", **kwargs):
        """Return a list of logs for device SN.

        Parameters
        ----------
        sn: string, required
            The device SN you would like data for
        return_type: string, required
            Return a list of json objects if set to 'json', or a dataframe if set to 'dataframe'
        params: dict, optional
            Query based on any column or parameter - see utils for further discussion.

        Returns
        -------
        list or dataframe

        Examples
        --------

        """
        assert(return_type in ("json", "dataframe")), "Bad return_type"

        data = self.fetch_data("log/{}/".format(sn), **kwargs)
        if return_type == "dataframe":
            data = list_to_dataframe(data)
        return data

    def get_cell_logs(self, sn, return_type="json", **kwargs):
        """Return a list of cellular logs for device SN.

        Parameters
        ----------
        sn: string, required
            The device SN you would like data for
        return_type: string, required
            Return a list of json objects if set to 'json', or a dataframe if set to 'dataframe'
        params: dict, optional
            Query based on any column or parameter - see utils for further discussion.

        Returns
        -------
        list or dataframe

        Examples
        --------

        """
        assert(return_type in ("json", "dataframe")), "Bad return_type"

        data = self.fetch_data("meta-data/cell-data/{}/".format(sn), **kwargs)
        if return_type == "dataframe":
            data = list_to_dataframe(data)
        return data

    def add_calibration_model(self, **kwargs):
        """Add a new calibration model.

        Parameters
        ----------
        params: dict, required
            A dictionary containing the relevant model upload information including
            the `sn`, `uploaded`, `name`, `comments`, `object_name`, `training_file`, 
            `param`, `metrics`, `model_params`, `tag`, and `name`.

        Returns
        -------
        model: dict
            A dictionary containing the model information that was uploaded.

        Examples
        --------
        >>> api = quantaq.legacy.QuantAQ()
        >>> api.add_calibration_model(params=dict())

        """
        return self._make_request("calibration-models/", type=POST, **kwargs)
    
    def get_calibration_models(self, sn, **kwargs):
        """Return the calibration model information for a given device.

        Parameters
        ----------
        sn: string, required
            The device serial number.

        Returns
        -------
        info: dict
            A dictionary containing calibration meta information for all models.

        Examples
        --------
        >>> api = quantaq.legacy.QuantAQ()
        >>> api.get_calibration_models(sn="SN000-001")

        """
        return self.fetch_data("calibration-models/{}".format(sn), **kwargs)
