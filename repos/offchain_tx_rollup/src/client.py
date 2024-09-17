
import time
from eth_account import Account
from web3.auto import w3

def sign_transaction(private_key, function_name, cost, params):
    account = Account.from_key(private_key)
    message = f"{function_name}:{cost}:{time.time()}:{params}"
    signed_message = w3.eth.account.sign_message(
        text=message,
        private_key=private_key
    )
    return signed_message.signature.hex()

def submit_transaction(function_name, cost, params):
    private_key = "YOUR_PRIVATE_KEY"  # Replace with actual private key
    signature = sign_transaction(private_key, function_name, cost, params)
    # Send to server (implement API call here)
    print(f"Transaction submitted: {function_name}, Cost: {cost}, Params: {params}")
    print(f"Signature: {signature}")

if __name__ == "__main__":
    submit_transaction("exampleFunction", 0.1, "param1,param2")
