import responses
import quantaq


NETWORK = {
    "name": "Network 1",
    "id": 1,
    "description": "",
    "created_on": "2023-11-16T00:00:00.000000+00:00",
    "organization": 1,
    "members": [],
    "devices": [],
}


@responses.activate
def test_networks_list():
    responses.add(responses.GET,"https://localhost/device-api/v1/orgs/1/networks/",
        status=200,
        json={
            "meta": {
                "first_url": "https://localhost/device-api/v1/orgs/1/networks/?page=1&per_page=2",
                "last_url": "https://localhost/device-api/v1/orgs/1/networks/?page=2&per_page=2",
                "next_url": "https://localhost/device-api/v1/orgs/1/networks/?page=2&per_page=2",
                "page": 1,
                "pages": 1,
                "per_page": 2,
                "prev_url": None,
                "total": 2
            },
            "data": [NETWORK],
        }
    )

    client = quantaq.client.APIClient(
        "https://localhost/device-api/", 
        api_key="a123", version="v1")

    resp = client.networks.list(org_id=1)

    assert type(resp) == list
    assert type(resp[0]) == dict
    assert len(resp) == 1


@responses.activate
def test_networks_get():
    responses.add(responses.GET, "https://localhost/device-api/v1/orgs/1/networks/1", 
        status=200, 
        json=NETWORK,
    )
    
    client = quantaq.client.APIClient(
        "https://localhost/device-api/", 
        api_key="a123", version="v1")

    # test the GET verb
    resp = client.networks.get(org_id=1, network_id=1)

    assert type(resp) == dict
