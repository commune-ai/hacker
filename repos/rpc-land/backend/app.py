
from flask import Flask, request, jsonify
from flask_cors import CORS
from web3 import Web3
import json

app = Flask(__name__)
CORS(app)

# In-memory storage for servers (replace with a database in production)
servers = []

# Ethereum node URL (replace with your own node or Infura URL)
ethereum_node_url = "https://mainnet.infura.io/v3/YOUR-PROJECT-ID"
w3 = Web3(Web3.HTTPProvider(ethereum_node_url))

@app.route('/api/servers', methods=['GET'])
def get_servers():
    return jsonify(servers)

@app.route('/api/servers', methods=['POST'])
def add_server():
    data = request.json
    if not data or 'name' not in data or 'url' not in data or 'ethereumKey' not in data:
        return jsonify({"error": "Invalid data"}), 400

    # Verify Ethereum key
    if not w3.isAddress(data['ethereumKey']):
        return jsonify({"error": "Invalid Ethereum address"}), 400

    new_server = {
        "id": len(servers) + 1,
        "name": data['name'],
        "url": data['url'],
        "ethereumKey": data['ethereumKey'],
        "whitelist": [],
        "blacklist": []
    }
    servers.append(new_server)
    return jsonify(new_server), 201

@app.route('/api/servers/<int:server_id>/forward', methods=['POST'])
def forward_request(server_id):
    server = next((s for s in servers if s['id'] == server_id), None)
    if not server:
        return jsonify({"error": "Server not found"}), 404

    # Implement forwarding logic here
    # This is a placeholder implementation
    return jsonify({"message": f"Request forwarded to {server['url']}"}), 200

@app.route('/api/servers/<int:server_id>/schema', methods=['GET'])
def get_schema(server_id):
    server = next((s for s in servers if s['id'] == server_id), None)
    if not server:
        return jsonify({"error": "Server not found"}), 404

    # Implement schema retrieval logic here
    # This is a placeholder implementation
    schema = {
        "type": "object",
        "properties": {
            "method": {"type": "string"},
            "params": {"type": "array"}
        }
    }
    return jsonify(schema), 200

@app.route('/api/servers/<int:server_id>/whitelist', methods=['POST'])
def add_to_whitelist(server_id):
    server = next((s for s in servers if s['id'] == server_id), None)
    if not server:
        return jsonify({"error": "Server not found"}), 404

    data = request.json
    if not data or 'ethereumKey' not in data:
        return jsonify({"error": "Invalid data"}), 400

    if w3.isAddress(data['ethereumKey']):
        server['whitelist'].append(data['ethereumKey'])
        return jsonify({"message": "Address added to whitelist"}), 200
    else:
        return jsonify({"error": "Invalid Ethereum address"}), 400

@app.route('/api/servers/<int:server_id>/blacklist', methods=['POST'])
def add_to_blacklist(server_id):
    server = next((s for s in servers if s['id'] == server_id), None)
    if not server:
        return jsonify({"error": "Server not found"}), 404

    data = request.json
    if not data or 'ethereumKey' not in data:
        return jsonify({"error": "Invalid data"}), 400

    if w3.isAddress(data['ethereumKey']):
        server['blacklist'].append(data['ethereumKey'])
        return jsonify({"message": "Address added to blacklist"}), 200
    else:
        return jsonify({"error": "Invalid Ethereum address"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
