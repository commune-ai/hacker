
import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_get_accounts():
    response = client.get("/accounts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_account():
    account_data = {
        "id": "test_account",
        "usdt_amount": 100.0
    }
    response = client.post("/accounts", json=account_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Account created successfully"}

def test_get_account():
    response = client.get("/accounts/test_account")
    assert response.status_code == 200
    assert response.json()["id"] == "test_account"
    assert response.json()["usdt_amount"] == 100.0

def test_update_account():
    update_data = {
        "id": "test_account",
        "usdt_amount": 200.0
    }
    response = client.put("/accounts/test_account", json=update_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Account updated successfully"}

    # Verify the update
    response = client.get("/accounts/test_account")
    assert response.status_code == 200
    assert response.json()["usdt_amount"] == 200.0

def test_get_nonexistent_account():
    response = client.get("/accounts/nonexistent")
    assert response.status_code == 404
    assert response.json() == {"detail": "Account not found"}
