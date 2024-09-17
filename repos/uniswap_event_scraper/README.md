
# Uniswap Event Scraper

This project scrapes events between two pools on Uniswap, focusing on order data from event logs. It uses Python and web3.py to interact with the Ethereum blockchain and retrieve event data.

## Features

- Scrape Uniswap events for specified pool pairs
- Store event data in JSON format
- Configurable date range for event retrieval
- Docker support for easy setup and execution

## Requirements

- Python 3.8+
- Docker (optional)

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/your-username/uniswap_event_scraper.git
   cd uniswap_event_scraper
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Ethereum node URL in `config.json`.

## Usage

1. Update `config.json` with your desired pool addresses and date range.
2. Run the scraper:
   ```
   python src/main.py
   ```

3. Check the `output` directory for the scraped event data in JSON format.

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

## Testing

Run tests using pytest:
```
pytest tests/
```

## License

This project is licensed under the MIT License.
