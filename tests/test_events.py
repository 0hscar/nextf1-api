import pytest
from src.main import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_next_event(client):
    response = client.get("/events/next")
    assert response.status_code in [200, 404]