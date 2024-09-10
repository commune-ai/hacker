
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/agents')
def get_agents():
    agents = [
        {"id": 1, "name": "Agent Smith", "specialty": "Negotiation"},
        {"id": 2, "name": "Agent Johnson", "specialty": "Infiltration"},
        {"id": 3, "name": "Agent Brown", "specialty": "Surveillance"}
    ]
    return jsonify(agents)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
