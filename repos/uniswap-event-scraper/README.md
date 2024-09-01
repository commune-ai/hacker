
# Uniswap Event Scraper

This project is a server that scrapes all events from the past N blocks of any ERC20 token pair on Uniswap. It allows you to retrieve historical data for any two token pairs with a customizable lookback period.

## Features

- Scrape Uniswap events for any ERC20 token pair
- Customizable lookback period (N blocks)
- Docker support for easy deployment

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/uniswap-event-scraper.git
   cd uniswap-event-scraper
   ```

2. Build the Docker image:
   ```
   ./scripts/build.sh
   ```

3. Run the server:
   ```
   ./scripts/run.sh
   ```

4. The server will be available at `http://localhost:3000`

## Usage

To scrape events for a token pair, make a GET request to the server:

```
GET /scrape?token0=0x...<address>&token1=0x...<address>&blocks=1000
```

- `token0`: Address of the first token in the pair
- `token1`: Address of the second token in the pair
- `blocks`: Number of blocks to look back (optional, default: 1000)

## License

This project is licensed under the MIT License.
