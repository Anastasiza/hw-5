import requests
import pytest
from pprint import pprint

id_brewery = ""

def test_all_breweries():
    global id_brewery
    response = requests.get("https://api.openbrewerydb.org/v1/breweries")
    id_brewery = response.json()[0]["id"]
    print(id_brewery)
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_brewery():
    response = requests.get(f"https://api.openbrewerydb.org/v1/breweries/{id_brewery}")
    assert response.status_code == 200
    assert response.json()["address_1"] is not None
    assert response.json()["latitude"] is not None
    assert response.json()["longitude"] is not None
    assert response.json()["city"] is not None


@pytest.mark.parametrize(("len_items","city_code", "city_name"),
                         [(3, "san_diego", "San Diego")])
def test_breweries_by_city(len_items, city_code, city_name):
    response = requests.get(f"https://api.openbrewerydb.org/v1/breweries?by_city={city_code}&per_page={len_items}")
    breweries = response.json()
    for brewery in breweries:
        assert brewery['city'] == city_name
    assert response.status_code == 200
    assert len(response.json()) == len_items


@pytest.mark.parametrize(("len_items","state_code", "state_name"),
                         [(3, "new_york", "New York")])
def test_by_state(len_items, state_code, state_name ):
    response = requests.get(f"https://api.openbrewerydb.org/v1/breweries?by_state={state_code}&per_page={len_items}")
    breweries = response.json()
    for brewery in breweries:
        assert brewery['state'] == state_name
    assert response.status_code == 200
    assert len(response.json()) == len_items

def test_by_postal():
    len_items = 3
    response = requests.get(f"https://api.openbrewerydb.org/v1/breweries?by_postal=44107&per_page={len_items}")
    breweries = response.json()
    pprint(breweries)
    for brewery in breweries:
        assert brewery['postal_code'][0:5] == "44107"
    assert response.status_code == 200
    assert len(response.json()) == len_items


