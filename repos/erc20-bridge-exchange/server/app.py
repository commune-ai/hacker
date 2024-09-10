
from flask import Flask, request, jsonify
from web3 import Web3
import os

app = Flask(__name__)

# Connect to Ethereum network (replace with your provider URL)
w3 = Web3(Web3.HTTPProvider(os.getenv('ETHEREUM_RPC_URL')))

# Contract address and ABI (replace with your deployed contract details)
CONTRACT_ADDRESS = os.getenv('CONTRACT_ADDRESS')
CONTRACT_ABI = [
    # Add your contract ABI here
]

contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

@app.route('/exchange', methods=['POST'])
def exchange_tokens():
    data = request.json
    amount = int(data['amount'])
    is_usdc = data['isUSDC']
    user_address = data['userAddress']

    try:
        # Call the smart contract function
        tx_hash = contract.functions.exchangeTokens(amount, is_usdc).transact({'from': user_address})
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        
        return jsonify({'success': True, 'transactionHash': receipt.transactionHash.hex()})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
