import responses
import quantaq
import os
import sys
import pandas as pd
import pytest

from quantaq.exceptions import QuantAQAPIException

@responses.activate
def test_users_list():
    responses.add(responses.GET, "https://localhost/device-api/v1/users/", 
        status=200, 
        json={
            "meta": {
                "first_url": "https://localhost/device-api/v1/users/?page=1&per_page=2",
                "last_url": "https://localhost/device-api/v1/users/?page=2&per_page=2",
                "next_url": "https://localhost/device-api/v1/users/?page=2&per_page=2",
                "page": 1,
                "pages": 1,
                "per_page": 2,
                "prev_url": None,
                "total": 2
            },
            "data": [
                {
                    "confirmed": True,
                    "email": "david.hagan@quant-aq.com",
                    "first_name": None,
                    "id": 2,
                    "is_administrator": True,
                    "last_name": None,
                    "last_seen": "2020-06-05T22:05:24.744063",
                    "member_since": "2020-06-05T22:05:24.744057",
                    "role": 5,
                    "username": "david.hagan"
                },
                {
                    "confirmed": True,
                    "email": "eben.cross@quant-aq.com",
                    "first_name": None,
                    "id": 3,
                    "is_administrator": True,
                    "last_name": None,
                    "last_seen": "2020-06-05T22:05:24.895573",
                    "member_since": "2020-06-05T22:05:24.895568",
                    "role": 5,
                    "username": "eben.cross"
                }
            ],
        }
    )
    
    client = quantaq.client.APIClient(
        "https://localhost/device-api/", 
        api_key="a123", version="v1")

    # test the GET verb
    resp = client.users.list()

    assert type(resp) == list
    assert type(resp[0]) == dict
    assert 'confirmed' in resp[0]
    assert len(resp) == 2

@responses.activate
def test_users_get():
    responses.add(responses.GET, "https://localhost/device-api/v1/users/1", 
        status=200, 
        json={
            "confirmed": True,
            "email": "david.hagan@quant-aq.com",
            "first_name": None,
            "id": 2,
            "is_administrator": True,
            "last_name": None,
            "last_seen": "2020-06-05T22:05:24.744063",
            "member_since": "2020-06-05T22:05:24.744057",
            "role": 5,
            "username": "david.hagan"
        },
    )
    
    client = quantaq.client.APIClient(
        "https://localhost/device-api/", 
        api_key="a123", version="v1")

    # test the GET verb
    resp = client.users.get(id=1)

    assert type(resp) == dict

@responses.activate
def test_users_list_paginate():
    responses.add(responses.GET, "https://localhost/device-api/v1/users/",
        status=200, json={
            "data": [
                {
                    "confirmed": True,
                    "email": "david.hagan@quant-aq.com",
                    "first_name": None,
                    "id": 2,
                    "is_administrator": True,
                    "last_name": None,
                    "last_seen": "2020-06-05T22:05:24.744063",
                    "member_since": "2020-06-05T22:05:24.744057",
                    "role": 5,
                    "username": "david.hagan"
                },
                {
                    "confirmed": True,
                    "email": "eben.cross@quant-aq.com",
                    "first_name": None,
                    "id": 3,
                    "is_administrator": True,
                    "last_name": None,
                    "last_seen": "2020-06-05T22:05:24.895573",
                    "member_since": "2020-06-05T22:05:24.895568",
                    "role": 5,
                    "username": "eben.cross"
                }
            ],
            "meta": {
                "first_url": "https://localhost/device-api/v1/users/?page=1&per_page=2",
                "last_url": "https://localhost/device-api/v1/users/?page=2&per_page=2",
                "next_url": "https://localhost/device-api/v1/users/?page=2&per_page=2",
                "page": 1,
                "pages": 2,
                "per_page": 2,
                "prev_url": None,
                "total": 3
            }
        })
    responses.add(responses.GET, "https://localhost/device-api/v1/users/",
        status=200, json={
            "data": [
                {
                    "confirmed": True,
                    "email": "david@davidhhagan.com",
                    "first_name": None,
                    "id": 1,
                    "is_administrator": True,
                    "last_name": None,
                    "last_seen": "2020-06-27T14:07:48.808618",
                    "member_since": "2020-06-05T22:05:24.612347",
                    "role": 5,
                    "username": "david"
                }
            ],
            "meta": {
                "first_url": "https://localhost/device-api/v1/users/?page=1&per_page=2",
                "last_url": "https://localhost/device-api/v1/users/?page=2&per_page=2",
                "next_url": None,
                "page": 2,
                "pages": 2,
                "per_page": 2,
                "prev_url": "https://localhost/device-api/v1/users/?page=1&per_page=2",
                "total": 3
            }
        })

    # make sure there were two calls
    client = quantaq.client.APIClient(
        "https://localhost/device-api/", api_key="a123", 
        version="v1")

    resp = client.users.list(per_page=2)

    assert len(resp) == 3
    assert len(responses.calls) == 2

    resp = client.users.list(per_page=1, limit=1, page=1)

    assert len(resp) == 1

@responses.activate
def test_users_update():
    responses.add(
        responses.PUT, "https://localhost/device-api/v1/users/1",
        status=200, json={
                "confirmed": True,
                "email": "david@davidhhagan.com",
                "first_name": None,
                "id": 1,
                "is_administrator": True,
                "last_name": "Hagan",
                "last_seen": "2020-06-27T14:30:29.106842",
                "member_since": "2020-06-05T22:05:24.612347",
                "role": 5,
                "username": "david"
        }
    )

    # make sure there were two calls
    client = quantaq.client.APIClient(
        "https://localhost/device-api/", api_key="a123", 
        version="v1")

    resp = client.users.update(id=1, last_name="Hagan")

    assert responses.calls[0].response.status_code == 200
    assert resp["last_name"] == "Hagan"