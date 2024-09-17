
import pytest
from unittest.mock import Mock, patch
from main import connect_to_ethereum, create_database, scrape_events, store_events

@pytest.fixture
def mock_web3():
    with patch('main.Web3') as mock:
        yield mock

@pytest.fixture
def mock_sqlite():
    with patch('main.sqlite3') as mock:
        yield mock

def test_connect_to_ethereum(mock_web3):
    connect_to_ethereum()
    mock_web3.HTTPProvider.assert_called_once()
    mock_web3.assert_called_once()

def test_create_database(mock_sqlite):
    create_database()
    mock_sqlite.connect.assert_called_once()
    mock_sqlite.connect().cursor().execute.assert_called_once()

def test_scrape_events(mock_web3):
    w3 = Mock()
    pool_address = "0x1234567890123456789012345678901234567890"
    start_block = 1000
    end_block = 2000
    
    scrape_events(w3, pool_address, start_block, end_block)
    w3.eth.get_logs.assert_called_once()

def test_store_events(mock_sqlite):
    conn = Mock()
    pool_address = "0x1234567890123456789012345678901234567890"
    events = [
        {'blockNumber': 1000, 'transactionHash': b'0x1234', 'data': 'event1'},
        {'blockNumber': 1001, 'transactionHash': b'0x5678', 'data': 'event2'}
    ]
    
    store_events(conn, pool_address, events)
    assert conn.cursor().execute.call_count == 2
    conn.commit.assert_called_once()

