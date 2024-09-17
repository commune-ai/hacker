
import json
from web3 import Web3
from datetime import datetime
from event_scraper import UniswapEventScraper

def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)

def main():
    config = load_config()
    w3 = Web3(Web3.HTTPProvider(config['ethereum_node_url']))
    
    scraper = UniswapEventScraper(w3)
    
    start_date = datetime.strptime(config['start_date'], '%Y-%m-%d')
    end_date = datetime.strptime(config['end_date'], '%Y-%m-%d')
    
    for pool_address in config['pool_addresses']:
        events = scraper.scrape_events(pool_address, start_date, end_date)
        
        output_file = f"output/events_{pool_address}_{start_date.date()}_{end_date.date()}.json"
        with open(output_file, 'w') as f:
            json.dump(events, f, indent=2)
        
        print(f"Events for pool {pool_address} saved to {output_file}")

if __name__ == "__main__":
    main()
