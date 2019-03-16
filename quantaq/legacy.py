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
        raise NotImplementedError("This method is not yet implemented.")
        # return self.fetch_data("devices/{}".format(sn), type=DELETE)

    def add_device(self, **kwargs):
        """Add a new device.

        Parameters
        ----------

        Returns
        -------

        Examples
        --------

        """
        raise NotImplementedError("This method is not yet implemented.")

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
        """Add new data.

        Parameters
        ----------

        Returns
        -------

        Examples
        --------

        """
        raise NotImplementedError("This method is not yet implemented.")
    
    def delete_data(self, sn, id, **kwargs):
        """Delete a data point.

        Parameters
        ----------

        Returns
        -------

        Examples
        --------

        """
        raise NotImplementedError("This method is not yet implemented.")

    def get_data(self, sn, return_type="json", final_data=True, **kwargs):
        """Return a list of data.

        Parameters
        ----------
        sn: string, required
            The device SN you would like data for
        return_type: string, required
            Return a list of json objects if set to 'json', or a dataframe if set to 'dataframe'
        final_data: bool
            If True, return the cleand/final data; if False, return the raw data (requires necessary permissions)
        params: dict, optional
            Query based on any column or parameter - see utils for further discussion.

        Returns
        -------
        list or dataframe

        Examples
        --------

        """
        assert(return_type in ("json", "dataframe")), "Bad return_type"
        endpoint = "devices/{}/data/".format(sn)
        if not final_data:
            endpoint += "raw/"

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
