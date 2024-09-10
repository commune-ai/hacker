
import pytest
from fastapi.testclient import TestClient
from server import app

client = TestClient(app)

def test_record_transaction():
    response = client.post("/transaction", json={
        "from_address": "0x1234567890123456789012345678901234567890",
        "amount": 100,
        "currency": "USDT"
    })
    assert response.status_code == 200
    assert response.json() == {"status": "Transaction recorded"}

def test_get_wallets():
    response = client.get("/wallets")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_get_spending_sheet():
    response = client.get("/spending_sheet")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_invalid_currency():
    response = client.post("/transaction", json={
        "from_address": "0x1234567890123456789012345678901234567890",
        "amount": 100,
        "currency": "BTC"
    })
    assert response.status_code == 400
    assert "Unsupported currency" in response.json()["detail"]
