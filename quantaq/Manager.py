# -*- coding: utf-8 -*-
from .baseapi import BaseAPI
from .Account import Account
from .Device import Device
from .baseapi import BaseAPI, PUT, DELETE, POST, GET

from .utils import list_to_dataframe

class QuantAQ(BaseAPI):
    """
    """
    def __init__(self, *args, **kwargs):
        super(QuantAQ, self).__init__(*args, **kwargs)

    def get_account(self):
        """Return the account associated with the API key being used.
        """
        return Account.get_object(token=self.token, endpoint=self.endpoint)

    def get_device(self, sn):
        """
        """
        return Device.get_object(sn=sn, token=self.token, endpoint=self.endpoint)

    def get_devices(self, return_type="json", **kwargs):
        """Return a list of all devices either as objects, json, or as a pd.DataFrame.
        """
        return_type = return_type.lower()
        if return_type not in ["json", "dataframe", "object"]:
            return_type = "json"
        
        data = self.fetch_data("devices/", **kwargs)
        if return_type == "dataframe":
            data = list_to_dataframe(data)
        if return_type == "object":
            devices = list()
            for each in data:
                dev = Device(**each)
                dev.token = self.token
                dev.endpoint = self.endpoint
                devices.append(dev)
            
            data = devices

        return data
    
    def post_device(self, params):
        """Add a new device.
        """
        data = self.fetch_data("devices/", type=POST, params=params)

        return Device(**data)
    

