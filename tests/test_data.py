import responses
import quantaq
import os
import sys
import pandas as pd
import pytest

from quantaq.exceptions import QuantAQAPIException

@responses.activate
def test_data_list():
    responses.add(responses.GET, "https://localhost/device-api/v1/devices/SN000-000/data/", 
        status=200, 
        json={
            "meta": {
                "first_url": "https://localhost/device-api/v1/devices/SN000-000/data/?page=1&per_page=2",
                "last_url": "https://localhost/device-api/v1/devices/SN000-000/data/?page=1&per_page=2",
                "next_url": None,
                "page": 1,
                "pages": 1,
                "per_page": 2,
                "prev_url": None,
                "total": 2
            },
            "data": [
                {
                    "co": 214.535431338815,
                    "co2": 480.390096687971,
                    "geo": {
                        "lat": 40.6000204324625,
                        "lon": 105.541939714035
                    },
                    "no": 10.200247314506,
                    "no2": 44.6936656602402,
                    "noise": 4.76532194833333,
                    "o3": 0.442416260227818,
                    "pm1": 5.47475036448307,
                    "pm10": 5.94977449893884,
                    "pm25": 5.6276302238071,
                    "pressure": 100819.890261942,
                    "rh_manifold": 6.62445621678516,
                    "sn": "SN000-000",
                    "solar": 2.49462009778851,
                    "temp_box": 45.0578371327661,
                    "temp_manifold": 33.3148097910394,
                    "timestamp": "2020-06-08T15:30:16.669152",
                    "timestamp_local": "2020-06-08T09:30:16.669152",
                    "tvoc": None,
                    "url": "https://localhost/device-api/v1/devices/SN000-000/data/10",
                    "wind_dir": 165.490010969395,
                    "wind_speed": 55.9829228072949
                },
                {
                    "co": 790.176776778167,
                    "co2": 479.654759364011,
                    "geo": {
                        "lat": 40.6000204324625,
                        "lon": 105.541939714035
                    },
                    "no": 24.7463880371725,
                    "no2": 62.1976466739495,
                    "noise": 8.49536012116147,
                    "o3": 10.0045781706225,
                    "pm1": 12.5814230319076,
                    "pm10": 21.718901275421,
                    "pm25": 14.2133728579415,
                    "pressure": 101324.263617099,
                    "rh_manifold": 81.8516598800883,
                    "sn": "SN000-000",
                    "solar": 7.80395850507548,
                    "temp_box": 14.0545590060536,
                    "temp_manifold": 0.36630906426483,
                    "timestamp": "2020-06-08T15:31:16.649641",
                    "timestamp_local": "2020-06-08T09:31:16.649641",
                    "tvoc": None,
                    "url": "https://localhost/device-api/v1/devices/SN000-000/data/9",
                    "wind_dir": 14.5751391589221,
                    "wind_speed": 46.8812222542059
                }
            ],
        }
    )
    
    client = quantaq.client.APIClient(
        "https://localhost/device-api/", 
        api_key="a123", version="v1")

    # test the GET verb
    resp = client.data.list(sn="SN000-000")

    assert type(resp) == list
    assert type(resp[0]) == dict
    assert 'co' in resp[0]
    assert len(resp) == 2

@responses.activate
def test_data_list_params():
    responses.add(responses.GET, "https://localhost/device-api/v1/devices/SN000-000/data/", 
        status=200, 
        json={
            "meta": {
                "first_url": "https://localhost/device-api/v1/devices/SN000-000/data/?page=1&per_page=2&filter=timestamp%2Clt%2C2020-06-15",
                "last_url": "https://localhost/device-api/v1/devices/SN000-000/data/?page=1&per_page=2&filter=timestamp%2Clt%2C2020-06-15",
                "next_url": None,
                "page": 1,
                "pages": 1,
                "per_page": 2,
                "prev_url": None,
                "total": 2
            },
            "data": [
                {
                    "co": 214.535431338815,
                    "co2": 480.390096687971,
                    "geo": {
                        "lat": 40.6000204324625,
                        "lon": 105.541939714035
                    },
                    "no": 10.200247314506,
                    "no2": 44.6936656602402,
                    "noise": 4.76532194833333,
                    "o3": 0.442416260227818,
                    "pm1": 5.47475036448307,
                    "pm10": 5.94977449893884,
                    "pm25": 5.6276302238071,
                    "pressure": 100819.890261942,
                    "rh_manifold": 6.62445621678516,
                    "sn": "SN000-000",
                    "solar": 2.49462009778851,
                    "temp_box": 45.0578371327661,
                    "temp_manifold": 33.3148097910394,
                    "timestamp": "2020-06-08T15:30:16.669152",
                    "timestamp_local": "2020-06-08T09:30:16.669152",
                    "tvoc": None,
                    "url": "https://localhost/device-api/v1/devices/SN000-000/data/10",
                    "wind_dir": 165.490010969395,
                    "wind_speed": 55.9829228072949
                },
                {
                    "co": 790.176776778167,
                    "co2": 479.654759364011,
                    "geo": {
                        "lat": 40.6000204324625,
                        "lon": 105.541939714035
                    },
                    "no": 24.7463880371725,
                    "no2": 62.1976466739495,
                    "noise": 8.49536012116147,
                    "o3": 10.0045781706225,
                    "pm1": 12.5814230319076,
                    "pm10": 21.718901275421,
                    "pm25": 14.2133728579415,
                    "pressure": 101324.263617099,
                    "rh_manifold": 81.8516598800883,
                    "sn": "SN000-000",
                    "solar": 7.80395850507548,
                    "temp_box": 14.0545590060536,
                    "temp_manifold": 0.36630906426483,
                    "timestamp": "2020-06-08T15:31:16.649641",
                    "timestamp_local": "2020-06-08T09:31:16.649641",
                    "tvoc": None,
                    "url": "https://localhost/device-api/v1/devices/SN000-000/data/9",
                    "wind_dir": 14.5751391589221,
                    "wind_speed": 46.8812222542059
                }
            ],
        }
    )

    client = quantaq.client.APIClient(
        "https://localhost/device-api/", 
        api_key="a123", version="v1")

    # test the GET verb
    resp = client.data.list(
        sn="SN000-000", stop="2020-06-15", start="2020-01-01",
        filter="co,lt,10000")

    assert type(resp) == list
    assert type(resp[0]) == dict
    assert 'co' in resp[0]
    assert len(resp) == 2

@responses.activate
def test_data_list_raw():
    responses.add(responses.GET, "https://localhost/device-api/v1/devices/SN000-000/data/raw/", 
        status=200, 
        json={
            "meta": {
                "first_url": "https://localhost/device-api/v1/devices/SN000-000/data/?page=1&per_page=2&filter=timestamp%2Clt%2C2020-06-15",
                "last_url": "https://localhost/device-api/v1/devices/SN000-000/data/?page=1&per_page=2&filter=timestamp%2Clt%2C2020-06-15",
                "next_url": None,
                "page": 1,
                "pages": 1,
                "per_page": 2,
                "prev_url": None,
                "total": 2
            },
            "data": [
                {
                    "bin0": 226.981332635404,
                    "bin1": 488.78728546421,
                    "bin2": 268.937393606539,
                    "bin3": 229.749245726731,
                    "bin4": 356.54546564323,
                    "bin5": 34.0198270215514,
                    "co2_raw": 872.590957292812,
                    "co_ae": 765.787103357745,
                    "co_diff": None,
                    "co_we": 685.691374109822,
                    "dew_point": 7.711121605969,
                    "flag": 2,
                    "geo": {
                        "lat": 40.6000204324625,
                        "lon": 105.541939714035
                    },
                    "no2_ae": 605.032546771419,
                    "no2_diff": None,
                    "no2_we": 411.322447975293,
                    "no_ae": 659.05186710844,
                    "no_diff": None,
                    "no_we": 952.019991677906,
                    "noise": 4.76532194833333,
                    "o3_ae": 855.810520096843,
                    "o3_diff": None,
                    "o3_we": 579.253555954903,
                    "opc_flow": 0.540979475271149,
                    "opc_sample_time": None,
                    "pressure": 100819.890261942,
                    "rh_manifold": 6.62445621678516,
                    "sn": "SN000-000",
                    "solar": 2.49462009778851,
                    "temp_box": 45.0578371327661,
                    "temp_manifold": 33.3148097910394,
                    "timestamp": "2020-06-08T15:30:16.669152",
                    "timestamp_local": "2020-06-08T09:30:16.669152",
                    "url": "https://localhost/device-api/v1/devices/SN000-000/data/raw/10",
                    "voc_raw": 430.325463304633,
                    "wind_dir": 165.490010969395,
                    "wind_speed": 55.9829228072949
                },
                {
                    "bin0": 622.608558774774,
                    "bin1": 738.970400977273,
                    "bin2": 91.1651905398073,
                    "bin3": 364.858429084212,
                    "bin4": 475.494741191533,
                    "bin5": 393.100588436105,
                    "co2_raw": 536.64224963332,
                    "co_ae": 588.665943231794,
                    "co_diff": None,
                    "co_we": 298.240622433652,
                    "dew_point": 4.48212742596445,
                    "flag": 1,
                    "geo": {
                        "lat": 40.6000204324625,
                        "lon": 105.541939714035
                    },
                    "no2_ae": 332.351239629168,
                    "no2_diff": None,
                    "no2_we": 477.995557589061,
                    "no_ae": 906.709183587395,
                    "no_diff": None,
                    "no_we": 415.876539828629,
                    "noise": 8.49536012116147,
                    "o3_ae": 485.318808232485,
                    "o3_diff": None,
                    "o3_we": 776.811635572823,
                    "opc_flow": 0.206268002779296,
                    "opc_sample_time": None,
                    "pressure": 101324.263617099,
                    "rh_manifold": 81.8516598800883,
                    "sn": "SN000-000",
                    "solar": 7.80395850507548,
                    "temp_box": 14.0545590060536,
                    "temp_manifold": 0.36630906426483,
                    "timestamp": "2020-06-08T15:31:16.649641",
                    "timestamp_local": "2020-06-08T09:31:16.649641",
                    "url": "https://localhost/device-api/v1/devices/SN000-000/data/raw/9",
                    "voc_raw": 264.07539915575,
                    "wind_dir": 14.5751391589221,
                    "wind_speed": 46.8812222542059
                }
            ],
        }
    )

    client = quantaq.client.APIClient(
        "https://localhost/device-api/", 
        api_key="a123", version="v1")

    # test the GET verb
    resp = client.data.list(
        sn="SN000-000", stop="2020-06-15", start="2020-01-01",
        filter="co_we,lt,10000", raw=True)

    assert type(resp) == list
    assert type(resp[0]) == dict
    assert 'co_we' in resp[0]
    assert len(resp) == 2

@responses.activate
def test_data_get():
    responses.add(responses.GET, "https://localhost/device-api/v1/devices/SN000-000/data/10",
        status=200, json={
            "co": 214.535431338815,
            "co2": 480.390096687971,
            "geo": {
                "lat": 40.6000204324625,
                "lon": 105.541939714035
            },
            "no": 10.200247314506,
            "no2": 44.6936656602402,
            "noise": 4.76532194833333,
            "o3": 0.442416260227818,
            "pm1": 5.47475036448307,
            "pm10": 5.94977449893884,
            "pm25": 5.6276302238071,
            "pressure": 100819.890261942,
            "rh_manifold": 6.62445621678516,
            "sn": "SN000-000",
            "solar": 2.49462009778851,
            "temp_box": 45.0578371327661,
            "temp_manifold": 33.3148097910394,
            "timestamp": "2020-06-08T15:30:16.669152",
            "timestamp_local": "2020-06-08T09:30:16.669152",
            "tvoc": None,
            "url": "https://localhost/device-api/v1/devices/SN000-000/data/10",
            "wind_dir": 165.490010969395,
            "wind_speed": 55.9829228072949
        })

    client = quantaq.client.APIClient(
        "https://localhost/device-api/", 
        api_key="a123", version="v1")

    # test the GET verb
    resp = client.data.get(sn="SN000-000", id=10)

    assert type(resp) == dict

@responses.activate
def test_data_get_raw():
    responses.add(responses.GET, "https://localhost/device-api/v1/devices/SN000-000/data/raw/10",
        status=200, json={
            "co": 214.535431338815,
            "co2": 480.390096687971,
            "geo": {
                "lat": 40.6000204324625,
                "lon": 105.541939714035
            },
            "no": 10.200247314506,
            "no2": 44.6936656602402,
            "noise": 4.76532194833333,
            "o3": 0.442416260227818,
            "pm1": 5.47475036448307,
            "pm10": 5.94977449893884,
            "pm25": 5.6276302238071,
            "pressure": 100819.890261942,
            "rh_manifold": 6.62445621678516,
            "sn": "SN000-000",
            "solar": 2.49462009778851,
            "temp_box": 45.0578371327661,
            "temp_manifold": 33.3148097910394,
            "timestamp": "2020-06-08T15:30:16.669152",
            "timestamp_local": "2020-06-08T09:30:16.669152",
            "tvoc": None,
            "url": "https://localhost/device-api/v1/devices/SN000-000/data/10",
            "wind_dir": 165.490010969395,
            "wind_speed": 55.9829228072949
        })

    client = quantaq.client.APIClient(
        "https://localhost/device-api/", 
        api_key="a123", version="v1")

    # test the GET verb
    resp = client.data.get(sn="SN000-000", id=10, raw=True)

    assert type(resp) == dict
   
@responses.activate 
def test_resampled_data():
    responses.add(responses.GET, "https://localhost/device-api/v1/devices/MOD-00100/data/resampled/?start_date=2024-01-01&end_date=2024-01-02&period=1h&per_page=100",
                  status=200, json={
                      "data": [
                          {
                              "co": 1.234,
                          },
                      ]
        }
    )

    client = quantaq.client.APIClient(
        "https://localhost/device-api/", api_key="a123", version="v1"
    )
    
    # Test the GET
    resp = client.data.byinterval(sn="MOD-00100", start_date="2024-01-01", end_date="2024-01-02", period="1h")
    
    assert type(resp) == dict