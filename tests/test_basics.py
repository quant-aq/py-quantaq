# import unittest
import responses
import quantaq
import os
import sys
import pandas as pd
import pytest

from quantaq.exceptions import QuantAQAPIException

# add additional tests using https://github.com/getsentry/responses

@responses.activate
def test_base(monkeypatch):
    responses.add(responses.GET, "https://api.quant-aq.com/device-api/v1/account", 
        json={"status": "success"}, status=200)

    # setup the API
    token = "A124324"
    client = quantaq.client.APIClient("https://api.quant-aq.com/device-api/", api_key=token, version="v1")

    # make sure you can init the client
    assert client.api_key == token
    assert client.base_url == "https://api.quant-aq.com/device-api/"
    assert client.version == "v1"

    # make sure client init fails with no token
    monkeypatch.setenv("QUANTAQ_APIKEY", "")
    with pytest.raises(QuantAQAPIException):
        client = quantaq.client.APIClient("https://test.com")

    # make sure url building works
    assert client.url("test") == "https://api.quant-aq.com/device-api/v1/test"

    # test the development api client
    client = quantaq.client.DevelopmentAPIClient(api_key="development")
    assert client.api_key == "development"
    assert client.base_url == "http://localhost:5000/device-api/"
    assert client.version == "v1"

    # test the staging api client
    client = quantaq.client.StagingAPIClient(api_key="staging")
    assert client.api_key == "staging"
    assert client.base_url == "https://dev.quant-aq.com/device-api/"
    assert client.version == "v1"

    # test the production api client
    client = quantaq.client.ProductionAPIClient(api_key="prod")
    assert client.api_key == "prod"
    assert client.base_url == "https://api.quant-aq.com/device-api/"
    assert client.version == "v1"

@responses.activate
def test_whoami():
    responses.add(responses.GET, "https://api.quant-aq.com/device-api/v1/account", 
        status=200, 
        json={
            "confirmed": True,
            "email": "david@davidhhagan.com",
            "first_name": None,
            "id": 1,
            "is_administrator": True,
            "last_name": None,
            "last_seen": "2020-06-27T03:31:39.722291",
            "member_since": "2020-06-05T22:05:24.612347",
            "role": 5,
            "username": "david"
            }
        )
    
    client = quantaq.client.APIClient(
        "https://api.quant-aq.com/device-api/", 
        api_key="a123", version="v1")

    # test the GET verb
    resp = client.whoami()

    assert resp["confirmed"] == True
    assert type(resp) == dict
    assert len(responses.calls) == 1
