# -*- coding: utf-8 -*-

"""
TODO:
  - update user account
  
"""

from .baseapi import BaseAPI


class Account(BaseAPI):
    """
    Params
    ------

    :param email:
    :param username:
    :param first_name:
    :param last_name:
    :param confirmed:
    :param last_seen:
    :param member_since:
    :param role:
    :param id:

    """
    def __init__(self, *args, **kwargs):
        self.email = None
        self.username = None
        self.confirmed = None
        self.first_name = None
        self.last_name = None
        self.member_since = None
        self.id = None
        self.last_seen = None

        super(Account, self).__init__(*args, **kwargs)

    @classmethod
    def get_object(cls, token=None, **kwargs):
        acct = cls(token=token, **kwargs)

        acct.load()

        return acct

    def load(self):
        """Load the user object from https://www.quant-aq.com/api/v1/account
        """
        data = self.fetch_data("account")

        for key in data.keys():
            setattr(self, key, data[key])

        return data

    def __repr__(self):
        return "<Account: {}>".format(self.username)
