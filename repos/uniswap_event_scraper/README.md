
# Uniswap Event Scraper

This project is a Python server that scrapes events from the past N blocks of any ERC20 token on Uniswap. It retrieves pair data for any two pairs with a customizable lookback history.

## Features

- Scrape Uniswap events for any ERC20 token
- Customizable lookback period (N blocks)
- Retrieve pair data for any two token pairs
- Docker support for easy deployment

## Requirements

- Python 3.8+
- Web3.py
- Flask
- Docker (optional)

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/uniswap_event_scraper.git
   cd uniswap_event_scraper
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Ethereum node URL in `config.py`.

## Usage

1. Run the server:
   ```
   python server.py
   ```

2. Access the API at `http://localhost:5000`:
   - `/scrape_events/<token_address>/<n_blocks>`: Scrape events for a specific token
   - `/pair_data/<token1_address>/<token2_address>/<n_blocks>`: Get pair data for two tokens

## Docker

To build and run the project using Docker:

1. Build the Docker image:
   ```
   ./scripts/build.sh
   ```

2. Run the Docker container:
   ```
   ./scripts/run.sh
   ```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
