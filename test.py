import requests
from pprint import pprint

response = requests.get("https://dog.ceo/api/breeds/list/all")
pprint(response.json())