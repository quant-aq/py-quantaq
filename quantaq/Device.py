# -*- coding: utf-8 -*-
from .baseapi import BaseAPI, PUT, DELETE, POST, GET
from .Data import ResearchData, Data
from .Log import Log

from .utils import list_to_dataframe


class Device(BaseAPI):
    def __init__(self, *args, **kwargs):
        self.sn = None

        super(Device, self).__init__(*args, **kwargs)

    @classmethod
    def get_object(cls, sn, **kwargs):
        device = cls(sn=sn, **kwargs)

        device.load()
        
        return device
    
    def load(self):
        """Load a device object from https://www.quant-aq.com/api/v1/devices/<sn>
        """
        data = self.fetch_data("devices/{}".format(self.sn))
        
        for key in data.keys():
            setattr(self, key, data[key])
        
        return data
    
    def destroy(self):
        """Delete the object from https://www.quant-aq.com/api/v1/devices/<sn>"""
        data = self.fetch_data(
            "devices/{}".format(self.sn), type=DELETE)
        
        return data
    
    def update(self, params):
        """Update a device. params should be a dictionary containing the updated fields.
        """
        data = self.fetch_data("devices/{}".format(self.sn), type=PUT, params=params)

        # update the object with the new params
        for key in data.keys():
            setattr(self, key, data[key])

    def get_data(self, return_type="json", researcher=False, **kwargs):
        """
        :param researcher: If you are a researcher, you have access to more in-depth data...
        """
        if return_type.lower() not in ["json", "dataframe", "object"]:
            return_type = "json"
        
        if researcher:
            data = self.fetch_data("devices/{}/data/raw/".format(self.sn), **kwargs)
        else:
            data = self.fetch_data("devices/{}/data/".format(self.sn), **kwargs)
        
        if return_type == "dataframe":
            data = list_to_dataframe(data)
        if return_type == "object":
            all_data = list()
            for each in data:
                if researcher:
                    point = ResearchData(**each)
                else:
                    point = Data(**each)
                point.token = self.token
                point.endpoint = self.endpoint
            
            data = all_data
 
        return data

    def get_metadata(self, return_type="json", **kwargs):
        """
        """
        raise NotImplementedError("This feature is not yet implemented")

    def get_logs(self, return_type="json", **kwargs):
        """
        """
        raise NotImplementedError("This feature is not yet implemented")
    
    def __repr__(self): #pragma: no cover
        return "<Device: {}>".format(self.sn)
