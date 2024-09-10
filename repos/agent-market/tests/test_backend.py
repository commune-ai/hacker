
import pytest
from backend.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_agents(client):
    response = client.get('/api/agents')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 3
    assert data[0]['name'] == 'Agent Smith'
