
import pytest
from server.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_exchange_tokens(client):
    response = client.post('/exchange', json={
        'amount': '1000000000000000000',
        'isUSDC': True,
        'userAddress': '0x1234567890123456789012345678901234567890'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] == True
    assert 'transactionHash' in data

def test_invalid_exchange(client):
    response = client.post('/exchange', json={
        'amount': '0',
        'isUSDC': True,
        'userAddress': '0x1234567890123456789012345678901234567890'
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data['success'] == False
    assert 'error' in data
