import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_get_events_success(client, monkeypatch):
    mock_data = {
        "_embedded": {
            "events": [
                {
                    "name": "Concierto de Prueba",
                    "id": "123",
                    "url": "https://ticketmaster.com/event/123",
                    "dates": {
                        "start": {
                            "localDate": "2025-10-01",
                            "localTime": "20:00"
                        }
                    },
                    "_embedded": {
                        "venues": [
                            {
                                "name": "Auditorio Nacional"
                            }
                        ]
                    }
                }
            ]
        }
    }

    class MockResponse:
        status_code = 200
        
        def json(self):
            return mock_data
        
        def raise_for_status(self):
            pass  # Do nothing for a successful response

    def mock_get(*args, **kwargs):
        return MockResponse()

    # Patch the requests.get method to use the mock_get
    monkeypatch.setattr("requests.get", mock_get)

    # Call the endpoint
    response = client.get("/api/events?city=Madrid")
    
    # Assert the response data if needed
    assert response.status_code == 200
    assert response.json() == mock_data  # You can add more assertions as needed


    def mock_get(*args, **kwargs):
        class MockResponse:
            status_code = 200
            def json(self):
                return mock_data
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    response = client.get("/api/events?city=Madrid")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert data[0]["name"] == "Concierto de Prueba"

def test_get_events_empty(client, monkeypatch):
    def mock_get(*args, **kwargs):
        class MockResponse:
            status_code = 200
            def json(self):
                return {}
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)
    response = client.get("/api/events?city=Desconocido")
    assert response.status_code == 200
    assert response.get_json() == []

def test_get_event_images_success(client, monkeypatch):
    mock_data = {
        "images": [
            {"url": "http://example.com/image1.jpg"},
            {"url": "http://example.com/image2.jpg"}
        ]
    }

    def mock_get(*args, **kwargs):
        class MockResponse:
            status_code = 200
            def json(self):
                return mock_data
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)
    response = client.get("/api/events/123/images")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert data[0]["url"] == "http://example.com/image1.jpg"

def test_get_event_images_empty(client, monkeypatch):
    def mock_get(*args, **kwargs):
        class MockResponse:
            status_code = 200
            def json(self):
                return {"images": []}
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)
    response = client.get("/api/events/000/images")
    assert response.status_code == 200
    assert response.get_json() == []
