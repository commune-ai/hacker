
import pytest
from app import app, players, leaderboard

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

def test_mine():
    # Simulate a player mining
    player_id = 'test_player'
    players[player_id] = {'score': 0, 'last_mine': 0}
    
    # Call the mine function
    from app import handle_mine
    handle_mine({'id': player_id})
    
    # Check if the player's score increased
    assert players[player_id]['score'] > 0

def test_leaderboard_update():
    # Add some test players
    players['player1'] = {'score': 100, 'last_mine': 0}
    players['player2'] = {'score': 200, 'last_mine': 0}
    players['player3'] = {'score': 150, 'last_mine': 0}
    
    # Update the leaderboard
    from app import update_leaderboard
    update_leaderboard()
    
    # Check if the leaderboard is correctly sorted
    assert leaderboard[0][0] == 'player2'
    assert leaderboard[1][0] == 'player3'
    assert leaderboard[2][0] == 'player1'
