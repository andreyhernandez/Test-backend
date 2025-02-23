import pytest
import requests

ENDPOINT="https://fake-json-api.mock.beeceptor.com/companies"

@pytest.mark.api
def test_back_get():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
    

@pytest.mark.api 
def test_response_json():
    response = requests.get(ENDPOINT)
    try:
        response.json()
    except requests.JSONDecodeError:
       print("La respuesta no es JSON.")
