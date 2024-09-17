
from fastapi.testclient import TestClient
from src.server import app

client = TestClient(app)

def test_submit_transaction():
    response = client.post("/submit_transaction", json={
        "function_name": "testFunction",
        "cost": 0.1,
        "params": "param1,param2",
        "signature": "0x1234...5678"  # Replace with a valid signature
    })
    assert response.status_code == 200
    assert response.json() == {"status": "Transaction recorded"}

def test_get_rollup():
    response = client.get("/get_rollup")
    assert response.status_code == 200
    assert "transactions" in response.json()
    assert "total_cost" in response.json()
