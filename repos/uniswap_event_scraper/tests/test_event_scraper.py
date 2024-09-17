
import pytest
from web3 import Web3
from src.event_scraper import UniswapEventScraper
from datetime import datetime, timedelta

@pytest.fixture
def w3():
    return Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR-PROJECT-ID'))

@pytest.fixture
def scraper(w3):
    return UniswapEventScraper(w3)

def test_scrape_events(scraper):
    pool_address = '0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8'
    start_date = datetime.now() - timedelta(days=1)
    end_date = datetime.now()
    
    events = scraper.scrape_events(pool_address, start_date, end_date)
    
    assert isinstance(events, list)
    assert len(events) > 0
    
    for event in events:
        assert 'event' in event
        assert 'blockNumber' in event
        assert 'transactionHash' in event
        assert 'args' in event

def test_get_block_number(scraper):
    date = datetime.now() - timedelta(days=1)
    block_number = scraper._get_block_number(date)
    
    assert isinstance(block_number, int)
    assert block_number > 0
