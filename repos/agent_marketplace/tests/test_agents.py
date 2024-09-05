
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_list_agents():
    response = client.get("/agents/")
    assert response.status_code == 200

def test_get_agent():
    response = client.get("/agents/1")
    assert response.status_code == 200

def test_create_agent():
    agent_data = {
        "name": "Test Agent",
        "description": "A test agent",
        "price": 9.99,
        "rating": 4.5
    }
    response = client.post("/agents/", json=agent_data)
    assert response.status_code == 200

def test_update_agent():
    agent_data = {
        "name": "Updated Agent",
        "description": "An updated test agent",
        "price": 19.99,
        "rating": 4.8
    }
    response = client.put("/agents/1", json=agent_data)
    assert response.status_code == 200

def test_delete_agent():
    response = client.delete("/agents/1")
    assert response.status_code == 200
