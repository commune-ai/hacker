
import pytest
from fastapi.testclient import TestClient
from app import app
from eth_account import Account
from eth_account.messages import encode_defunct

client = TestClient(app)

def test_execute_transaction():
    # Create a test account
    test_account = Account.create()
    
    # Create a test transaction
    tx = {
        "function_name": "test_function",
        "cost": 1.5,
        "timestamp": int(time.time()),
        "parameters": {"param1": "value1"},
    }
    
    # Sign the transaction
    message = f"{tx['function_name']}{tx['cost']}{tx['timestamp']}{tx['parameters']}"
    message_hash = encode_defunct(text=message)
    signed_message = test_account.sign_message(message_hash)
    tx["signature"] = signed_message.signature.hex()
    
    # Send the transaction
    response = client.post("/execute", json=tx)
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_get_rollup():
    response = client.get("/rollup")
    assert response.status_code == 200
    assert "transactions" in response.json()
    assert "total_cost" in response.json()

