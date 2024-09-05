
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_list_transactions():
    response = client.get("/transactions/")
    assert response.status_code == 200

def test_get_transaction():
    response = client.get("/transactions/1")
    assert response.status_code == 200

def test_create_transaction():
    transaction_data = {
        "user_id": 1,
        "agent_id": 1,
        "amount": 9.99,
        "timestamp": "2023-04-22T12:00:00Z"
    }
    response = client.post("/transactions/", json=transaction_data)
    assert response.status_code == 200
