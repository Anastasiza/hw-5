import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
    )
    parser.addoption(
        "--status_code",
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")

@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")



def test_1(url,status_code):
    response = requests.get(url)
    assert int(status_code) == response.status_code
