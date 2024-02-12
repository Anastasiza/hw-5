import requests
import pytest



def test_list_all_breeds():
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    response_body = response.json()
    assert response.status_code == 200
    assert len(response_body['message']) > 0
    assert response_body['status'] == 'success'

def test_random_image():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    assert response.status_code == 200
    assert response.json()['message'][0:8] == 'https://'

def test_breed_image():
    response = requests.get("https://dog.ceo/api/breed/hound/images")
    response_body = response.json()
    assert response.status_code == 200
    assert len(response_body['message']) > 0

@pytest.mark.parametrize(("breed"),[("hound")])
def test_breed_list(breed):
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/list")
    response_body = response.json()
    assert response.status_code == 200
    assert len(response_body['message']) > 0
    assert response_body['status'] == 'success'
@pytest.mark.parametrize(("breed"),[("affenpinscher")])
def test_breed_random(breed):
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")
    assert response.status_code == 200
    assert response.json()['message'][0:8] == 'https://'



