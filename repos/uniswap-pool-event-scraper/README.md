
# Uniswap Pool Event Scraper

This project scrapes all events between two pools on Uniswap, allowing you to analyze order data through event information.

## Features

- Connects to Ethereum network using Web3.py
- Scrapes events from specified Uniswap V3 pools
- Stores event data in a local database
- Provides analysis and visualization of order data

## Requirements

- Python 3.8+
- Docker
- Ethereum node access (e.g., Infura)

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/your-username/uniswap-pool-event-scraper.git
   cd uniswap-pool-event-scraper
   ```

2. Create a `.env` file in the project root and add your Ethereum node URL:
   ```
   ETHEREUM_NODE_URL=https://mainnet.infura.io/v3/YOUR-PROJECT-ID
   ```

3. Build the Docker image:
   ```
   ./scripts/build.sh
   ```

4. Run the scraper:
   ```
   ./scripts/run.sh
   ```

## Usage

Modify the `config.py` file to specify the Uniswap V3 pool addresses you want to scrape. Then run the scraper using the provided scripts.

## Testing

Run the tests using:
```
docker run uniswap-pool-event-scraper pytest
```

## License

This project is licensed under the MIT License.
