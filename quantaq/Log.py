# -*- coding: utf-8 -*-
from .baseapi import BaseAPI, PUT, DELETE, POST, GET


class Log(BaseAPI):
    def __init__(self, *args, **kwargs):
        self.sn = kwargs.pop("sn", None)
        self.id = kwargs.pop("id", None)

        super(Log, self).__init__(*args, **kwargs)

    @classmethod
    def get_object(cls, sn, id, **kwargs):
        log = cls(sn=sn, id=id, **kwargs)

        log.load()

        return data

    def load(self):
        """
        """
        data = self.fetch_data(
            "log/{}/{}".format(self.sn, self.id))

        for key in data.keys():
            setattr(self, key, data[key])

        return data

    def destroy(self):
        """
        """
        data = self.fetch_data(
            "log/{}/{}".format(self.sn, self.id), type=DELETE)
        
        return data

    def update(self, params):
        """
        """
        data = self.fetch_data("log/{}/{}".format(self.sn, self.id),
                               type=PUT, params=params)

        for key in data.keys():
            setattr(self, key, data[key])

    def __repr__(self):
        return "<Log: {}/{}>".format(self.sn, self.id)
