import responses
import quantaq
import os
import sys
import pandas as pd
import pytest

from quantaq.exceptions import QuantAQAPIException

@responses.activate
def test_teams_list():
    responses.add(responses.GET, "https://localhost/device-api/v1/teams/", 
        status=200, 
        json={
            "meta": {
                "first_url": "https://localhost/device-api/v1/teams/?page=1&per_page=2",
                "last_url": "https://localhost/device-api/v1/teams/?page=2&per_page=2",
                "next_url": "https://localhost/device-api/v1/teams/?page=2&per_page=2",
                "page": 1,
                "pages": 1,
                "per_page": 2,
                "prev_url": None,
                "total": 2
            },
            "data": [
                {
                    "name": "Team 1",
                    "description": "",
                    "admins": [],
                    "devices": [],
                    "members": []
                },
            ],
        }
    )
    
    client = quantaq.client.APIClient(
        "https://localhost/device-api/", 
        api_key="a123", version="v1")

    # test the GET verb
    resp = client.teams.list()

    assert type(resp) == list
    assert type(resp[0]) == dict
    assert len(resp) == 1

@responses.activate
def test_teams_get():
    responses.add(responses.GET, "https://localhost/device-api/v1/teams/1", 
        status=200, 
        json={
            "name": "team-1",
            "description": "",
            "members": [],
            "id": 1,
            "admins": [],
            "devices": [],
        },
    )
    
    client = quantaq.client.APIClient(
        "https://localhost/device-api/", 
        api_key="a123", version="v1")

    # test the GET verb
    resp = client.teams.get(id=1)

    assert type(resp) == dict
