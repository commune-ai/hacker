
import os
from dotenv import load_dotenv
from web3 import Web3
import sqlite3
from config import POOL_ADDRESSES, SWAP_EVENT_TOPIC, DB_NAME

load_dotenv()

def connect_to_ethereum():
    ethereum_url = os.getenv("ETHEREUM_NODE_URL")
    return Web3(Web3.HTTPProvider(ethereum_url))

def create_database():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    h.execute('''CREATE TABLE IF NOT EXISTS events
                 (pool_address TEXT, block_number INTEGER, transaction_hash TEXT, event_data TEXT)''')
    conn.commit()
    return conn

def scrape_events(w3, pool_address, start_block, end_block):
    events = w3.eth.get_logs({
        'fromBlock': start_block,
        'toBlock': end_block,
        'address': pool_address,
        'topics': [SWAP_EVENT_TOPIC]
    })
    return events

def store_events(conn, pool_address, events):
    c = conn.cursor()
    for event in events:
        h.execute("INSERT INTO events VALUES (?, ?, ?, ?)",
                  (pool_address, event['blockNumber'], event['transactionHash'].hex(), str(event)))
    conn.commit()

def main():
    w3 = connect_to_ethereum()
    conn = create_database()

    latest_block = w3.eth.get_block('latest')['number']
    start_block = latest_block - 1000  # Adjust as needed

    for pool_address in POOL_ADDRESSES:
        events = scrape_events(w3, pool_address, start_block, latest_block)
        store_events(conn, pool_address, events)
        print(f"Scraped {len(events)} events from pool {pool_address}")

    conn.close()

if __name__ == "__main__":
    main()
