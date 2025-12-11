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
    assert client.base_url == "https://api.quant-aq.dev/device-api/"
    assert client.version == "v1"

    # test the production api client
    client = quantaq.client.ProductionAPIClient(api_key="prod")
    assert client.api_key == "prod"
    assert client.base_url == "https://api.quant-aq.com/device-api/"
    assert client.version == "v1"


@responses.activate
def test_rate_limit_retry():
    def set_responses(num_fails):
        responses.reset()
        # succeed first page, fail next one x times, succeed second page, succeed last one.
        responses.add(
            responses.GET,
            "https://localhost/device-api/v1/devices/BLAH/data/?per_page=1",
            json={
                "meta": {
                    "first_url": "https://localhost/device-api/v1/devices/BLAH/data/?per_page=1&page=1",
                    "last_url": "https://localhost/device-api/v1/devices/BLAH/data/?per_page=1&page=3",
                    "next_url": "https://localhost/device-api/v1/devices/BLAH/data/?per_page=1&page=2",
                    "page": 1,
                    "pages": 3,
                    "per_page": 1,
                    "prev_url": None,
                    "total": 3,
                },
                "data": [{"blah": 1}],
            },
            status=200,
        )
        for n in range(num_fails):
            responses.add(
                responses.GET,
                "https://localhost/device-api/v1/devices/BLAH/data/?per_page=1&page=2",
                json={"error": "too many requests", "message": "blah blah"},
                status=429,
            )
        responses.add(
            responses.GET,
            "https://localhost/device-api/v1/devices/BLAH/data/?per_page=1&page=2",
            json={
                "meta": {
                    "first_url": "https://localhost/device-api/v1/devices/BLAH/data/?per_page=1&page=1",
                    "last_url": "https://localhost/device-api/v1/devices/BLAH/data/?per_page=1&page=3",
                    "next_url": "https://localhost/device-api/v1/devices/BLAH/data/?per_page=1&page=3",
                    "page": 2,
                    "pages": 3,
                    "per_page": 1,
                    "prev_url": "https://localhost/device-api/v1/devices/BLAH/data/?per_page=1&page=1",
                    "total": 3,
                },
                "data": [{"blah": 2}],
            },
            status=200,
        )
        responses.add(
            responses.GET,
            "https://localhost/device-api/v1/devices/BLAH/data/?per_page=1&page=3",
            json={
                "meta": {
                    "first_url": "https://localhost/device-api/v1/devices/BLAH/data/?per_page=1&page=1",
                    "last_url": "https://localhost/device-api/v1/devices/BLAH/data/?per_page=1&page=3",
                    "next_url": None,
                    "page": 3,
                    "pages": 3,
                    "per_page": 1,
                    "prev_url": "https://localhost/device-api/v1/devices/BLAH/data/?per_page=1&page=2",
                    "total": 3,
                },
                "data": [{"blah": 3}],
            },
            status=200,
        )

    client = quantaq.client.APIClient(
        "https://localhost/device-api/",
        api_key="a123",
        version="v1",
    )

    # if it fails twice, we're good
    set_responses(num_fails=2)
    resp = client.data.list(sn="BLAH", per_page=1)
    assert len(resp) == 3
    assert resp == [
        {'blah': 1},
        {'blah': 2},
        {'blah': 3},
    ]
    assert len(responses.calls) == 5

    # if it fails three times, that's surfaced
    set_responses(num_fails=3)
    with pytest.raises(QuantAQAPIException, match="Rate limiting retries exceeded."):
        client.data.list(sn="BLAH", per_page=1)
    assert len(responses.calls) == 4


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
