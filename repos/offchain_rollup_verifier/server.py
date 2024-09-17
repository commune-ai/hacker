
from flask import Flask, request, jsonify
from web3 import Web3
from eth_account.messages import encode_defunct
import json
import time
from config import ETHEREUM_NODE_URL

app = Flask(__name__)
w3 = Web3(Web3.HTTPProvider(ETHEREUM_NODE_URL))

transactions = []

@app.route('/execute', methods=['POST'])
def execute_function():
    data = request.json
    message = data['message']
    signature = data['signature']

    # Verify the signature
    message_hash = encode_defunct(text=json.dumps(message))
    signer = w3.eth.account.recover_message(message_hash, signature=signature)

    # Verify timestamp is recent
    if int(time.time()) - message['timestamp'] > 300:  # 5 minutes
        return jsonify({"error": "Transaction expired"}), 400

    # Execute the function (placeholder)
    result = execute_offchain_function(message['function'], message['params'])

    # Store the transaction
    transactions.append({
        "signer": signer,
        "function": message['function'],
        "cost": message['cost'],
        "timestamp": message['timestamp'],
        "params": message['params']
    })

    return jsonify({"result": result})

def execute_offchain_function(function_name, params):
    # Placeholder for actual function execution
    return f"Executed {function_name} with params {params}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
