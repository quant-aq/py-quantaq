# -*- coding: utf-8 -*-
import os
import json
import quantaq
import requests
import logging
from requests.models import Response
from typing import Optional, Union

try:
    import urlparse
except ImportError:
    from urllib import parse as urlparse

from .exceptions import QuantAQAPIException

GET = "GET"
PUT = "PUT"
DELETE = "DELETE"
POST = "POST"

class ClientBase(object):
    """A client for accessing the QuantAQ API."""
    def __init__(
        self, 
        api_key=None, 
        base_url=None, 
        version=None) -> None:
        """
        Initialize the QuantAQ API.

        :param str api_key: API key to authenticate with
        :param str base_url: The base url for API calls, defaults to 'https://api.quant-aq.com/device-api'
        :param str version: The API version, defaults to 'v1'

        :returns: QuantAQ Client
        :rtype: quantaq.client.ClientBase
        """
        # check for credentials
        self.api_key = api_key or os.environ.get("QUANTAQ_APIKEY", None)
        self.base_url = base_url
        self.version = version

        self._logger = logging.getLogger(__name__)

        self._users = None
        self._devices = None
        self._teams = None
        self._data = None
        self._logs = None
        self._cellular = None
        self._models = None

        if not self.api_key:
            raise QuantAQAPIException("You must provide a valid API key")

    @property
    def headers(self):
        return {
            "Content-Type": "application/json"
        }
    
    @property
    def auth(self):
        return (self.api_key, "")

    def url(self, endpoint : str) -> str:
        """Build and return the url"""
        return urlparse.urljoin("{}{}/".format(self.base_url, self.version), endpoint)

    def paginate(self, endpoint, verb, params, data):
        """Iterate over all pages to get all of the data. If results aren't
        paginated, just return the results.

        :param endpoint str:
        :param verb str: the HTTP method
        :param params dict:
        :param data list:

        """
        all_data = data.get("data")

        # iterate and get more data (if needed)
        while data.get("meta", dict()).get("next_url"):
            endpoint, q = data.get("meta").get("next_url").split("?", 1)

            for k, v in urlparse.parse_qs(q).items():
                params[k] = v
            
            # re-issue the request for the next page
            data = self.request(endpoint, verb, params).json()

            # append the data
            [all_data.append(item) for item in data.get('data')]

        return all_data

    def request(self, endpoint, verb=GET, params=None, **kwargs) -> Response:
        """Make a request to the QuantAQ API.

        :param str endpoint: Fully qualified URL
        :param str verb: HTTP method
        :param dict[str, str] params: Query string parameters

        :returns: Response from the QuantAQ API
        :rtype: requests.Response
        """
        params = dict() if params is None else params

        # if certain kwargs are present, add them to params
        params = {**params, **kwargs}

        identity = lambda x: x
        json_dumps = lambda x: json.dumps(x)

        lookup = {
            GET: (requests.get, {}, "params", identity),
            POST: (requests.post, self.headers, "data", json_dumps),
            PUT: (requests.put, self.headers, "data", json_dumps),
            DELETE: (requests.delete, self.headers, "data", json_dumps)
        }

        requests_method, headers, payload, transform = lookup[verb]

        # create a logging string
        agent = "{0}/{1} {2}/{3}".format(
                quantaq.__name__, quantaq.__version__, 
                requests.__name__, requests.__version__)

        # set the kwargs
        kwargs = {"headers": headers, payload: transform(params)}

        # build the url
        url = self.url(endpoint)

        # log the request
        self._logger.debug("{} {} {}: {} {}".format(type, url, payload, params, agent))

        return requests_method(url, auth=self.auth, **kwargs)

    def requests(self, endpoint, verb=GET, params=dict(), **kwargs):
        """Request, but for many of them (i.e. deals with pagination)
        """
        # set defaults
        if verb == GET:
            params.setdefault("per_page", 100)

        # add start and end to the kwargs
        filter = kwargs.pop("filter", [])
        if filter != []:
            filter = filter.split(";")

        if "start" in kwargs.keys():
            filter.append("timestamp,ge," + kwargs.pop("start"))
    
        if "stop" in kwargs.keys():
            filter.append("timestamp,le," + kwargs.pop("stop"))

        # add filter to the kwargs
        if len(filter) > 0:
            kwargs = {**kwargs, **dict(filter=";".join(filter))}

        params = {**params, **kwargs}

        # make the request
        r = self.request(endpoint, verb, params)

        # check for errors
        if r.status_code not in (200, 201, 202):
            raise QuantAQAPIException("Bad response ({}): {}".format(r.status_code, r.json()))
    
        # get the json response
        try:
            data = r.json()
        except ValueError:
            raise QuantAQAPIException("Could not decode the json response")

        # deal with pagination if needed
        pages = data.get("meta", None)
        if pages:
            if pages.get("next_url") and pages.get("page") != pages.get("pages"):
                data = self.paginate(endpoint, verb, params, data)
            else:
                data = data.get('data')
        
        return data

    def __str__(self): #pragma: no cover
        return "<%s>" % self.__class__.__name__


class APIClient(ClientBase):
    """
    """
    def __init__(self, base_url, api_key=None, version=None):
        super(APIClient, self).__init__(api_key, base_url, version)

    def whoami(self):
        """Return information about the current account user

        Examples
        --------

        >>> client = quantaq.QuantAQAPIClient()
        >>> client.whoami()

        """
        return self.requests("account")

    @property
    def users(self):
        """"""
        if self._users is None:
            from .endpoints.users import Users
            self._users = Users(self)
        return self._users

    @property
    def teams(self):
        """"""
        if self._teams is None:
            from .endpoints.teams import Teams
            self._teams = Teams(self)
        return self._teams

    @property
    def devices(self):
        """"""
        if self._devices is None:
            from .endpoints.devices import Devices
            self._devices = Devices(self)
        return self._devices

    @property
    def data(self):
        """"""
        if self._data is None:
            from .endpoints.data import Data
            self._data = Data(self)
        return self._data

    @property
    def logs(self):
        """"""
        if self._logs is None:
            from .endpoints.logs import Logs
            self._logs = Logs(self)
        return self._logs

    @property
    def cellular(self):
        """"""
        if self._cellular is None:
            from .endpoints.cellular import Cellular
            self._cellular = Cellular(self)
        return self._cellular
    
    @property
    def models(self):
        """"""
        if self._models is None:
            from .endpoints.models import Models
            self._models = Models(self)
        return self._models


class DevelopmentAPIClient(APIClient):
    def __init__(self, api_key=None) -> None:
        super().__init__("http://localhost:5000/device-api/", 
                            version="v1", api_key=api_key)


class StagingAPIClient(APIClient):
    def __init__(self, api_key=None) -> None:
        super().__init__("https://dev.quant-aq.com/device-api/", 
                            version="v1", api_key=api_key)


class ProductionAPIClient(APIClient):
    def __init__(self, api_key=None) -> None:
        super().__init__("https://api.quant-aq.com/device-api/", 
                            version="v1", api_key=api_key)



