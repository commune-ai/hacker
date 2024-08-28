
from flask import Flask, jsonify, request
from flask_cors import CORS
from models import db, Bounty, User
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
db.init_app(app)

@app.route('/api/bounties', methods=['GET'])
def get_bounties():
    bounties = Bounty.query.all()
    return jsonify([bounty.to_dict() for bounty in bounties])

@app.route('/api/bounties', methods=['POST'])
def create_bounty():
    data = request.json
    new_bounty = Bounty(title=data['title'], description=data['description'], reward=data['reward'])
    db.session.add(new_bounty)
    db.session.commit()
    return jsonify(new_bounty.to_dict()), 201

@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
