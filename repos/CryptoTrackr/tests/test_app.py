
import pytest
from backend.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_record_donation(client):
    response = client.post('/api/donations', json={
        'from': '0x1234567890123456789012345678901234567890',
        'amount': '1.5',
        'currency': 'ETH'
    })
    assert response.status_code == 200
    assert response.json['success'] == True

def test_get_donations(client):
    response = client.get('/api/donations/0x1234567890123456789012345678901234567890')
    assert response.status_code == 200
    assert 'donations' in response.json

def test_get_all_donations(client):
    response = client.get('/api/admin/donations')
    assert response.status_code == 200
    assert 'donations' in response.json
