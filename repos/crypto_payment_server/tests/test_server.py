
import pytest
from server import CryptoPaymentServer

@pytest.fixture
def server():
    return CryptoPaymentServer()

def test_accept_payment(server):
    # Implement test logic here
    pass

def test_get_token_price(server):
    # Implement test logic here
    pass

def test_swap_to_stablecoin(server):
    # Implement test logic here
    pass

