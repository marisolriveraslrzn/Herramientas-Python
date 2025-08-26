import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_weather(client):
    response = client.get('/weather/Madrid')
    assert response.status_code == 200

def test_post_weather(client):
    response = client.post('/weather/NuevaCiudad', json={"temperature": 25, "condition": "Sunny"})
    assert response.status_code == 201
