import requests
import pytest
from pprint import pprint


def test_getting_resource():
    post_number = 1
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_number}")
    response_body = response.json()
    assert response.status_code == 200
    assert response_body['body'] is not None
    assert response_body['id'] is not None
    assert response_body['title'] is not None
    assert response_body['userId'] is not None


def test_all_resources():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200
    assert len(response.json()) > 0


@pytest.mark.parametrize( ('title', 'body', 'userId'),
                          [('foo', 'bar', 1)])
def test_creating_resource(title, body, userId):
    json = {
        'title': title,
        'body': body,
        'userId': userId,
    }
    headers = {
        'Content-type': 'application/json; charset=UTF-8',
    }

    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=json, headers=headers)

    pprint(response.json())
    assert response.status_code == 201
    assert response.json()['body'] == body
    assert response.json()['title'] == title
    assert response.json()['userId'] == userId


@pytest.mark.parametrize(('title', 'body', 'userId'),
                         [('foo', 'bar', 1)])
def test_updating_resource(title, body, userId):
    json = {
        'title': title,
        'body': body,
        'userId': userId,
    }
    headers = {
        'Content-type': 'application/json; charset=UTF-8',
    }
    response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=json, headers=headers)
    assert response.status_code == 200
    assert response.json()['body'] == json['body']
    assert response.json()['title'] == json['title']
    assert response.json()['userId'] == json['userId']


def test_delete_resource():
    response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
