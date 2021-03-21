import pytest

from apiApp1 import app

client = app.test_client()

def test_sample():
    jsonData = {
        "username": "ted",
        "targetDevice": "taperoll",
        "requestDetails": "NA",
        "targetIntensity": 100
    }
    response = client.post('/app-request', json=jsonData)
    expectedResponse = '{"Result": "Success"}'
    assert str(expectedResponse) == response.get_data(as_text=True)
