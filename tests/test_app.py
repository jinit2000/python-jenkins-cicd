import json
from app.app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    json_data = json.loads(response.data)
    assert json_data["message"] == "Jenkins CI/CD Pipeline Working with Flask on port 5001!"
