
import pytest
from client import Client

def test_sign_transaction():
    client = Client("0x1234567890123456789012345678901234567890123456789012345678901234")
    message, signature = client.sign_transaction("test_function", 0.1, {"param1": "value1"})
    
    assert "function" in message
    assert "cost" in message
    assert "timestamp" in message
    assert "params" in message
    assert len(signature) == 132  # 65 bytes in hex

def test_call_server_function(mocker):
    mock_post = mocker.patch('requests.post')
    mock_post.return_value.json.return_value = {"result": "success"}

    client = Client("0x1234567890123456789012345678901234567890123456789012345678901234")
    result = client.call_server_function("test_function", 0.1, {"param1": "value1"})

    assert result == {"result": "success"}
    mock_post.assert_called_once()
