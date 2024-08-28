
from flask import Flask, request, jsonify
from flask_cors import CORS
from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

w3 = Web3(Web3.HTTPProvider(os.getenv('ETHEREUM_NODE_URL')))

ERC20_ABI = [{"constant":True,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"}]

erc20_contract = w3.eth.contract(address=os.getenv('ERC20_CONTRACT_ADDRESS'), abi=ERC20_ABI)

servers = []
admins = set()

def check_token_balance(address):
    balance = erc20_contract.functions.balanceOf(address).call()
    return balance >= int(os.getenv('REQUIRED_TOKEN_BALANCE'))

@app.route('/api/servers', methods=['GET'])
def get_servers():
    user_address = request.args.get('address')
    if check_token_balance(user_address):
        return jsonify(servers)
    return jsonify({"error": "Insufficient token balance"}), 403

@app.route('/api/servers', methods=['POST'])
def add_server():
    user_address = request.json.get('address')
    if user_address not in admins:
        return jsonify({"error": "Unauthorized"}), 403
    
    server = request.json.get('server')
    servers.append(server)
    return jsonify({"message": "Server added successfully"})

@app.route('/api/servers/<int:index>', methods=['DELETE'])
def remove_server(index):
    user_address = request.json.get('address')
    if user_address not in admins:
        return jsonify({"error": "Unauthorized"}), 403
    
    if 0 <= index < len(servers):
        del servers[index]
        return jsonify({"message": "Server removed successfully"})
    return jsonify({"error": "Invalid server index"}), 400

@app.route('/api/admin', methods=['POST'])
def become_admin():
    user_address = request.json.get('address')
    if check_token_balance(user_address):
        admins.add(user_address)
        return jsonify({"message": "You are now an admin"})
    return jsonify({"error": "Insufficient token balance"}), 403

if __name__ == '__main__':
    app.run(debug=True)
