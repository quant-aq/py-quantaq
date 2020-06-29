import responses
import quantaq
import os
import sys
import pandas as pd
import pytest

from quantaq.exceptions import QuantAQAPIException

@responses.activate
def test_models_get():
    responses.add(responses.GET, "https://localhost/device-api/v1/calibration-models/SN000-000", 
        status=200, 
        json={
                "co": {
                    "calibration": None,
                    "id": 1,
                    "model": None,
                    "param": "co"
                }, 
            }
    )
    
    client = quantaq.client.APIClient(
        "https://localhost/device-api/", 
        api_key="a123", version="v1")

    # test the GET verb
    resp = client.models.get(sn="SN000-000")

    assert type(resp) == dict

@responses.activate
def test_models_add():
    responses.add(responses.POST, "https://localhost/device-api/v1/calibration-models/", 
        status=201, 
        json={}
    )
    
    client = quantaq.client.APIClient(
        "https://localhost/device-api/", 
        api_key="a123", version="v1")

    # test the GET verb
    resp = client.models.add(
        sn="SN000-000", 
        param='co',
        name='test-co-model',
        object_name='file1.sav',
        training_file='obj1/training.csv',
        error=dict(r2=0.87, rmse=.97, mae=.5)
        )

    assert type(resp) == dict
    assert responses.calls[0].response.status_code == 201
