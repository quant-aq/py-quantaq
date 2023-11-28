import responses
import quantaq


ORGANIZATION = {
    "name": "Organization 1",
    "id": 1,
    "description": "",
    "created_on": "2023-11-16T00:00:00.000000+00:00",
    "sandbox": "false",
    "members": [],
    "devices": [],
    "networks": [],
}


@responses.activate
def test_organizations_list():
    responses.add(responses.GET,"https://localhost/device-api/v1/orgs/",
        status=200,
        json={
            "meta": {
                "first_url": "https://localhost/device-api/v1/orgs/?page=1&per_page=2",
                "last_url": "https://localhost/device-api/v1/orgs/?page=2&per_page=2",
                "next_url": "https://localhost/device-api/v1/orgs/?page=2&per_page=2",
                "page": 1,
                "pages": 1,
                "per_page": 2,
                "prev_url": None,
                "total": 2
            },
            "data": [ORGANIZATION],
        }
    )

    client = quantaq.client.APIClient(
        "https://localhost/device-api/", 
        api_key="a123", version="v1")

    resp = client.organizations.list()

    assert type(resp) == list
    assert type(resp[0]) == dict
    assert len(resp) == 1


@responses.activate
def test_organizations_get():
    responses.add(responses.GET, "https://localhost/device-api/v1/orgs/1", 
        status=200, 
        json=ORGANIZATION,
    )
    
    client = quantaq.client.APIClient(
        "https://localhost/device-api/", 
        api_key="a123", version="v1")

    # test the GET verb
    resp = client.organizations.get(id=1)

    assert type(resp) == dict
