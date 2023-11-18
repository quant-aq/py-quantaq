import responses
import quantaq
import os
import sys
import pandas as pd
import pytest

from quantaq.exceptions import QuantAQAPIException

@responses.activate
def test_devices_list():
    responses.add(responses.GET, "https://localhost/device-api/v1/devices/", 
        status=200, 
        json={
            "meta": {
                "first_url": "https://localhost/device-api/v1/devices/?page=1&per_page=2",
                "last_url": "https://localhost/device-api/v1/devices/?page=2&per_page=2",
                "next_url": "https://localhost/device-api/v1/devices/?page=2&per_page=2",
                "page": 1,
                "pages": 1,
                "per_page": 2,
                "prev_url": None,
                "total": 2
            },
            "data": [
                {
                    "city": "Fort Collins",
                    "country": "US",
                    "created": "2020-06-08T15:38:17.274489",
                    "description": None,
                    "geo": {
                        "lat": 40.9844188816344,
                        "lon": 105.561207967016
                    },
                    "id": 2,
                    "last_seen": "2020-06-08T15:39:16.923105",
                    "model": "arisense_v200",
                    "n_datapoints": 10,
                    "outdoors": True,
                    "owner_id": None,
                    "private": False,
                    "sn": "SN000-001",
                    "status": "ACTIVE",
                    "timezone": "US/Mountain",
                    "url": "https://localhost/device-api/v1/devices/SN000-001"
                },
                {
                    "city": "Fort Collins",
                    "country": "US",
                    "created": "2020-06-08T15:38:17.275411",
                    "description": None,
                    "geo": {
                        "lat": 41.5456805631496,
                        "lon": 105.795622755017
                    },
                    "id": 3,
                    "last_seen": "2020-06-08T15:39:17.154547",
                    "model": "arisense_v200",
                    "n_datapoints": 10,
                    "outdoors": True,
                    "owner_id": None,
                    "private": False,
                    "sn": "SN000-002",
                    "status": "ACTIVE",
                    "timezone": "US/Mountain",
                    "url": "https://localhost/device-api/v1/devices/SN000-002"
                },
                {
                    "city": "Fort Collins",
                    "country": "US",
                    "created": "2020-06-08T15:38:17.265789",
                    "description": "",
                    "geo": {
                        "lat": 40.6,
                        "lon": 105.54
                    },
                    "id": 1,
                    "last_seen": "2020-06-08T15:40:01.174522",
                    "model": "arisense_v200",
                    "n_datapoints": 10,
                    "outdoors": True,
                    "owner_id": 1,
                    "private": True,
                    "sn": "SN000-000",
                    "status": "ACTIVE",
                    "timezone": "US/Mountain",
                    "url": "https://localhost/device-api/v1/devices/SN000-000"
                }
            ],
        }
    )
    
    client = quantaq.client.APIClient(
        "https://localhost/device-api/", 
        api_key="a123", version="v1")

    # test the GET verb
    resp = client.devices.list()

    assert type(resp) == list
    assert type(resp[0]) == dict
    assert 'status' in resp[0]
    assert len(resp) == 3

    # brief check that org_id/network_id are passed on as query parameters
    resp = client.devices.list(org_id=1, network_id=1)
    assert 'org_id=1&network_id=1' in responses.calls[1].request.url
    assert type(resp) == list

@responses.activate
def test_devices_get():
    responses.add(responses.GET, "https://localhost/device-api/v1/devices/SN000-000", 
        status=200, 
        json={
            "city": "Fort Collins",
            "country": "US",
            "created": "2020-06-08T15:38:17.265789",
            "description": "",
            "geo": {
                "lat": 40.6,
                "lon": 105.54
            },
            "id": 1,
            "last_seen": "2020-06-08T15:40:01.174522",
            "model": "arisense_v200",
            "n_datapoints": 10,
            "outdoors": True,
            "owner_id": 1,
            "private": True,
            "sn": "SN000-000",
            "status": "ACTIVE",
            "timezone": "US/Mountain",
            "url": "https://localhost/device-api/v1/devices/SN000-000"
        },
    )
    
    client = quantaq.client.APIClient(
        "https://localhost/device-api/", 
        api_key="a123", version="v1")

    # test the GET verb
    resp = client.devices.get(sn="SN000-000")

    assert type(resp) == dict

@responses.activate
def test_devices_update():
    responses.add(
        responses.PUT, "https://localhost/device-api/v1/devices/SN000-000",
        status=200, json={
                "city": "Fort Collins",
                "country": "UK",
                "created": "2020-06-08T15:38:17.265789",
                "description": "",
                "geo": {
                    "lat": 40.6,
                    "lon": 105.54
                },
                "id": 1,
                "last_seen": "2020-06-08T15:40:01.174522",
                "model": "arisense_v200",
                "n_datapoints": 10,
                "outdoors": True,
                "owner_id": 1,
                "private": True,
                "sn": "SN000-000",
                "status": "ACTIVE",
                "timezone": "US/Mountain",
                "url": "https://localhost/device-api/v1/devices/SN000-000"
        }
    )

    # make sure there were two calls
    client = quantaq.client.APIClient(
        "https://localhost/device-api/", api_key="a123", 
        version="v1")

    resp = client.devices.update(sn="SN000-000", country="UK")

    assert responses.calls[0].response.status_code == 200
    assert resp["country"] == "UK"


@responses.activate
def test_devices_add():
    responses.add(
        responses.POST, "https://localhost/device-api/v1/devices/",
        status=201, json={
                "city": "Fort Collins",
                "country": "UK",
                "created": "2020-06-08T15:38:17.265789",
                "description": "",
                "geo": {
                    "lat": 40.6,
                    "lon": 105.54
                },
                "id": 4,
                "last_seen": "2020-06-08T15:40:01.174522",
                "model": "arisense_v200",
                "n_datapoints": 10,
                "outdoors": True,
                "owner_id": 1,
                "private": True,
                "sn": "SN000-TMP",
                "status": "INACTIVE",
                "timezone": "US/Mountain",
                "url": "https://localhost/device-api/v1/devices/SN000-TMP"
        }
    )

    # make sure there were two calls
    client = quantaq.client.APIClient(
        "https://localhost/device-api/", api_key="a123", 
        version="v1")

    resp = client.devices.add(
        sn="SN000-000", 
        country="UK", 
        model="arisense_v200"
    )

    assert responses.calls[0].response.status_code == 201
    assert resp["country"] == "UK"
    assert resp["model"] == "arisense_v200"


@responses.activate
def test_devices_drop():
    responses.add(
        responses.DELETE, "https://localhost/device-api/v1/devices/SN000-TMP",
        status=202, json={"device dropped": "success"}
    )

    # make sure there were two calls
    client = quantaq.client.APIClient(
        "https://localhost/device-api/", api_key="a123", 
        version="v1")

    resp = client.devices.drop(sn="SN000-TMP")

    assert type(resp) == dict
    assert responses.calls[0].response.status_code == 202