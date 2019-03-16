# -*- coding: utf-8 -*-
from .baseapi import BaseAPI, PUT, DELETE, POST, GET


class Data(BaseAPI):
    def __init__(self, *args, **kwargs):
        self.sn = kwargs.pop("sn", None)
        self.id = kwargs.pop("id", None)

        super(Data, self).__init__(*args, **kwargs)

    @classmethod
    def get_object(cls, sn, id, **kwargs):
        data = cls(sn=sn, id=id, **kwargs)

        data.load()

        return data

    def load(self):
        """
        """
        data = self.fetch_data(
            "devices/{}/data/{}".format(self.sn, self.id))

        for key in data.keys():
            setattr(self, key, data[key])

        return data

    def destroy(self):
        """
        """
        raise NotImplementedError("This method is not yet implemented")

    def update(self, params):
        """
        """
        data = self.fetch_data("devices/{}/data/{}".format(self.sn, self.id),
                               type=PUT, params=params)

        for key in data.keys():
            setattr(self, key, data[key])

    def __repr__(self):
        return "<Data: {}/{}>".format(self.sn, self.id)


class ResearchData(BaseAPI):
    def __init__(self, *args, **kwargs):
        self.sn = kwargs.pop("sn", None)
        self.id = kwargs.pop("id", None)

        super(ResearchData, self).__init__(*args, **kwargs)

    @classmethod
    def get_object(cls, sn, id, **kwargs):
        data = cls(sn=sn, id=id, **kwargs)

        data.load()

        return data
    
    def load(self):
        """
        """
        data = self.fetch_data("devices/{}/data/raw/{}".format(self.sn, self.id))

        for key in data.keys():
            setattr(self, key, data[key])

        return data
    
    def destroy(self):
        """
        """
        raise NotImplementedError("This method is not yet implemented")
    
    def update(self, params):
        """
        """
        data = self.fetch_data("devices/{}/data/raw/{}".format(self.sn, self.id), 
            type=PUT, params=params)
        
        for key in data.keys():
            setattr(self, key, data[key])
    
    def __repr__(self):
        return "<ResearchData: {}/{}>".format(self.sn, self.id)
