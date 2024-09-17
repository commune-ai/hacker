
import pytest
from src.client import sign_transaction

def test_sign_transaction():
    private_key = "0x0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
    function_name = "testFunction"
    cost = 0.1
    params = "param1,param2"
    
    signature = sign_transaction(private_key, function_name, cost, params)
    assert isinstance(signature, str)
    assert len(signature) == 132  # 64 bytes (32 for r, 32 for s) + 1 byte for v, represented as hex
