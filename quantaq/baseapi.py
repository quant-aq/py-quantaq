# -*- coding: utf-8 -*-

import os
import requests
import logging
import json

from . import __name__, __version__

try:
    import urlparse
except ImportError:
    from urllib import parse as urlparse

GET = "GET"
PUT = "PUT"
DELETE = "DELETE"
POST = "POST"

class TokenError(Exception):
    pass

class NotFoundError(Exception):
    pass

class NotPermittedError(Exception):
    pass

class BadRequestError(Exception):
    pass

class JsonReadError(Exception):
    pass

class DataReadError(Exception):
    pass



class BaseAPI(object):
    """Basic API wrapper class"""
    def __init__(self, token=None, *args, **kwargs):
        if token:
            self.token = token
        else:
            self.token = os.environ.get("QUANTAQ_APIKEY", None)
        
        self.endpoint = kwargs.pop("endpoint", "https://api.quant-aq.com/device-api/")
        self.version = kwargs.pop("version", "v1")

        self._logger = logging.getLogger(__name__)

        for attr in kwargs.keys():
            setattr(self, attr, kwargs[attr])
    
    @property
    def url_prefix(self):
        return urlparse.urljoin(self.endpoint, "{}/".format(self.version))

    def _make_request(self, endpoint, type=GET, params=None):
        """Perform an API request.

        Examples
        --------

        >>> resp = api._make_request(endpoint="/device", params=dict(per_page=2))
        """
        if params is None:
            params = dict()

        if not self.token:
            raise TokenError("No API token provided.")
        
        # join the url
        url = urlparse.urljoin(self.url_prefix, endpoint)

        headers = {"Content-Type": "application/json"}
        identity = lambda x: x
        json_dumps = lambda x: json.dumps(x)

        lookup = {
            GET: (requests.get, {}, "params", identity),
            POST: (requests.post, headers, "data", json_dumps),
            PUT: (requests.put, headers, "data", json_dumps),
            DELETE: (requests.delete, headers, "data", json_dumps)
        }

        requests_method, headers, payload, transform = lookup[type]

        # create a logging string
        agent = "{0}/{1} {2}/{3}".format(
                "py-quantaq", __version__, 
                requests.__name__, requests.__version__)

        # set the kwargs
        kwargs = {"headers": headers, payload: transform(params)}

        # set the authentication params
        auth = (self.token, "")

        # log the debug string
        self._logger.debug("{} {} {}: {} {}".format(type, url, payload, params, agent))
        # print("{} {} {}: {} {}".format(type, url, payload, params, agent))

        return requests_method(url, auth=auth, **kwargs)

    def _deal_with_pagination(self, endpoint, method, params, data):
        """Perform multiple calls to retrieve all data when the results are paginated.
        If results aren't in fact paginated, return just the results.
        """
        all_data = data.get("data")

        # iterate and make more get requests
        while data.get("meta", {}).get("next_url"):
            url, query = data.get("meta").get("next_url").split("?", 1)

            for k, v in urlparse.parse_qs(query).items():
                params[k] = v
            
            # re-issue the request for the next page
            data = self._make_request(url, method, params).json()

            # append the data to all_data
            [all_data.append(item) for item in data.get("data")]

        return all_data
    
    def fetch_data(self, endpoint, type=GET, params=None):
        """Make a get call - this method handles pagination.
        """
        if params is None:
            params = dict()

        # set a default number of items to return per_page
        if type == "GET":
            params.setdefault("per_page", 200)
        
        # make the request
        r = self._make_request(endpoint, type, params)

        # check for errors
        if r.status_code == 404:
            raise NotFoundError()
        if r.status_code == 403:
            raise NotPermittedError()
        if r.status_code == 400:
            raise BadRequestError()
        
        try:
            data = r.json()
        except ValueError:
            raise JsonReadError("Could not decode the json data")

        if not r.ok:
            raise DataReadError("Could not retrieve data from quant-aq.com")
        
        # deal with pagination if needed
        pages = data.get("meta", None)
        if pages is not None:
            if pages.get("next_url") and pages.get("page") != pages.get("pages"):
                data = self._deal_with_pagination(endpoint, type, params, data)
            else:
                data = data.get("data")
    
        return data

    def __str__(self):
        return "<%s>" % self.__class__.__name__

    def __unicode(self):
        return u"<%s>" % self.__str__
    
    def __repr__(self): #pragma: no cover
        return str(self)
