
import time
import json
from web3 import Web3
from eth_account.messages import encode_defunct
from eth_account import Account
import requests
from config import SERVER_HOST, SERVER_PORT

class Client:
    def __init__(self, private_key):
        self.account = Account.from_key(private_key)
        self.w3 = Web3()

    def sign_transaction(self, function_name, cost, params):
        timestamp = int(time.time())
        message = {
            "function": function_name,
            "cost": cost,
            "timestamp": timestamp,
            "params": params
        }
        message_hash = encode_defunct(text=json.dumps(message))
        signed_message = self.account.sign_message(message_hash)
        return message, signed_message.signature.hex()

    def call_server_function(self, function_name, cost, params):
        message, signature = self.sign_transaction(function_name, cost, params)
        payload = {
            "message": message,
            "signature": signature
        }
        response = requests.post(f"http://{SERVER_HOST}:{SERVER_PORT}/execute", json=payload)
        return response.json()

if __name__ == "__main__":
    client = Client("YOUR_PRIVATE_KEY")
    result = client.call_server_function("example_function", 0.1, {"param1": "value1"})
    print(result)
