
from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
import random
import time
from solana.rpc.async_api import AsyncClient
from solana.transaction import Transaction
from solana.system_program import TransferParams, transfer
import asyncio
import config

app = Flask(__name__)
socketio = SocketIO(app)

players = {}
leaderboard = []

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    player_id = request.sid
    players[player_id] = {'score': 0, 'last_mine': time.time()}
    socketio.emit('player_joined', {'id': player_id})

@socketio.on('disconnect')
def handle_disconnect():
    player_id = request.sid
    if player_id in players:
        del players[player_id]
    update_leaderboard()

@socketio.on('mine')
def handle_mine(data):
    player_id = request.sid
    current_time = time.time()
    if current_time - players[player_id]['last_mine'] >= config.MINING_INTERVAL:
        mining_power = random.randint(1, 10)
        players[player_id]['score'] += mining_power
        players[player_id]['last_mine'] = current_time
        socketio.emit('mine_result', {'id': player_id, 'power': mining_power, 'score': players[player_id]['score']})
        update_leaderboard()

def update_leaderboard():
    global leaderboard
    leaderboard = sorted(players.items(), key=lambda x: x[1]['score'], reverse=True)[:config.LEADERBOARD_SIZE]
    socketio.emit('leaderboard_update', {'leaderboard': leaderboard})

async def reward_top_player():
    if leaderboard:
        top_player = leaderboard[0][0]
        async with AsyncClient(config.SOLANA_NETWORK) as client:
            transaction = Transaction().add(transfer(TransferParams(
                from_pubkey=config.AUTHORITY_KEYPAIR.public_key,
                to_pubkey=players[top_player]['wallet'],
                lamports=int(config.TOKEN_REWARD_AMOUNT * 1e9)  # Convert to lamports
            )))
            await client.send_transaction(transaction, config.AUTHORITY_KEYPAIR)
        socketio.emit('reward_sent', {'player': top_player, 'amount': config.TOKEN_REWARD_AMOUNT})

if __name__ == '__main__':
    socketio.run(app, debug=True)
