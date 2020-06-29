import responses
import quantaq
import os
import sys
import pandas as pd
import pytest

from quantaq.exceptions import QuantAQAPIException

@responses.activate
def test_logs_list():
    responses.add(responses.GET, "https://localhost/device-api/v1/log/SN000-000/", 
        status=200, 
        json={
            "meta": {
                "first_url": "https://localhost/device-api/v1/log/SN000-000/?page=1&per_page=2",
                "last_url": "https://localhost/device-api/v1/log/SN000-000/?page=1&per_page=2",
                "next_url": None,
                "page": 1,
                "pages": 1,
                "per_page": 2,
                "prev_url": None,
                "total": 2
            },
            "data": [
                {
                    "level": "INFO",
                    "message": "test message",
                    "millis": 1000,
                    "sn": "SN000-000",
                    "timestamp": "2020-06-27T23:07:53.185276",
                    "url": "https://localhost/device-api/v1/log/SN000-000/1"
                }
            ],
        }
    )
    
    client = quantaq.client.APIClient(
        "https://localhost/device-api/", 
        api_key="a123", version="v1")

    # test the GET verb
    resp = client.logs.list(sn="SN000-000")

    assert type(resp) == list
    assert type(resp[0]) == dict
    assert 'millis' in resp[0]
    assert len(resp) == 1

@responses.activate
def test_logs_get():
    responses.add(responses.GET, "https://localhost/device-api/v1/log/SN000-000/1", 
        status=200, 
        json={
            "level": "INFO",
            "message": "test message",
            "millis": 1000,
            "sn": "SN000-000",
            "timestamp": "2020-06-27T23:07:53.185276",
            "url": "https://localhost/device-api/v1/log/SN000-000/1"
        }
    )
    
    client = quantaq.client.APIClient(
        "https://localhost/device-api/", 
        api_key="a123", version="v1")

    # test the GET verb
    resp = client.logs.get(sn="SN000-000", id=1)

    assert type(resp) == dict
    assert 'millis' in resp

@responses.activate
def test_logs_update():
    responses.add(responses.PUT, "https://localhost/device-api/v1/log/SN000-000/1", 
        status=200, 
        json={
            "level": "WARNING",
            "message": "test message",
            "millis": 1000,
            "sn": "SN000-000",
            "timestamp": "2020-06-27T23:07:53.185276",
            "url": "https://localhost/device-api/v1/log/SN000-000/1"
        }
    )
    
    client = quantaq.client.APIClient(
        "https://localhost/device-api/", 
        api_key="a123", version="v1")

    # test the GET verb
    resp = client.logs.update(sn="SN000-000", id=1, level="WARNING")

    assert type(resp) == dict
    assert 'millis' in resp
    assert resp['level'] == 'WARNING'


@responses.activate
def test_logs_delete():
    responses.add(responses.DELETE, "https://localhost/device-api/v1/log/SN000-000/1", 
        status=200, 
        json={"log deleted": "success"})
    
    client = quantaq.client.APIClient(
        "https://localhost/device-api/", 
        api_key="a123", version="v1")

    # test the GET verb
    resp = client.logs.drop(sn="SN000-000", id=1)

    assert type(resp) == dict
    