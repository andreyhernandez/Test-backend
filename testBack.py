import pytest
import requests
from jsonschema import validate, ValidationError

ENDPOINT="https://fake-json-api.mock.beeceptor.com/companies"
company_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "address": {"type": "string"},
        "zip": {"type": "string"},
        "country": {"type": "string"},
        "employeeCount": {"type": "integer"},
        "industry": {"type": "string"},
        "marketCap": {"type": "integer"},
        "domain": {"type": "string"},
        "logo": {"type": "string"},
        "ceoName": {"type": "string"}
        
    },
    "required": ["id", "name", "address", "zip","country","employeeCount","industry","marketCap","domain","logo","ceoName"]
}


@pytest.mark.api
def test_back_get():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
    

@pytest.mark.api
def test_response_json():
    response = requests.get(ENDPOINT)
    try:
        data = response.json()
        assert isinstance(data, list), "La respuesta debe ser una lista de objetos JSON"
        
        for item in data:
            validate(instance=item, schema=company_schema)
    
    except ValidationError as e:
        pytest.fail(f"Error de validación del esquema JSON: {e}")