
import pytest
from server import app
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_execute_function(client, mocker):
    mock_recover = mocker.patch('web3.eth.account.recover_message')
    mock_recover.return_value = "0x1234567890123456789012345678901234567890"

    data = {
        "message": {
            "function": "test_function",
            "cost": 0.1,
            "timestamp": 1234567890,
            "params": {"param1": "value1"}
        },
        "signature": "0x1234567890"
    }

    response = client.post('/execute', json=data)
    assert response.status_code == 200
    assert "result" in json.loads(response.data)
