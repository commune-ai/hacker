
from web3 import Web3
import time

class RateLimiter:
    def __init__(self, contract_address, token_address, web3_provider='http://localhost:8545'):
        self.w3 = Web3(Web3.HTTPProvider(web3_provider))
        self.contract = self.w3.eth.contract(address=contract_address, abi=RateLimiter.abi)
        self.token = self.w3.eth.contract(address=token_address, abi=ERC20_ABI)

    def check_rate_limit(self, user_address):
        return self.contract.functions.checkRateLimit(user_address).call()

    def update_last_request_time(self, user_address):
        tx_hash = self.contract.functions.updateLastRequestTime(user_address).transact({'from': user_address})
        self.w3.eth.wait_for_transaction_receipt(tx_hash)

    def get_token_balance(self, user_address):
        return self.token.functions.balanceOf(user_address).call()

# Add ERC20_ABI and RateLimiter.abi here
