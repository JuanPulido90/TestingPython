import requests
from requests.auth import HTTPBasicAuth


def test_authentication():

    response = requests.get('https://login.dev.jupiterone.io/', auth =HTTPBasicAuth('nadiahamdytest@cassini.testinator.com', '$Test123'))
    print(response.text)
    print(response.status_code)
