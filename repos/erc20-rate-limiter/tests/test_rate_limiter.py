
import pytest
from web3 import Web3
from server.rate_limiter import RateLimiter

@pytest.fixture
def web3():
    return Web3(Web3.HTTPProvider('http://localhost:8545'))

@pytest.fixture
def rate_limiter(web3):
    # Deploy contracts and create RateLimiter instance
    # This is a simplified example, you'll need to deploy your contracts first
    contract_address = '0x...'
    token_address = '0x...'
    return RateLimiter(contract_address, token_address)

def test_check_rate_limit(web3, rate_limiter):
    account = web3.eth.accounts[0]
    assert rate_limiter.check_rate_limit(account) == True

def test_update_last_request_time(web3, rate_limiter):
    account = web3.eth.accounts[0]
    rate_limiter.update_last_request_time(account)
    assert rate_limiter.check_rate_limit(account) == False

def test_get_token_balance(web3, rate_limiter):
    account = web3.eth.accounts[0]
    balance = rate_limiter.get_token_balance(account)
    assert balance >= 0
