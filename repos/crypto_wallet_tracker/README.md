
# Crypto Wallet Tracker

This project is a Python server that accepts Ethereum, USDT, and USDC transactions. It records the wallets that send USD and maintains a spending sheet. It also includes an Agent class with a generate function and a call_cost parameter.

## Features

- Accept Ethereum, USDT, and USDC transactions
- Record sender wallets and transaction amounts
- Maintain a spending sheet
- Agent class with generate function and call_cost parameter

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the server: `python server.py`

## Docker

To build and run the project using Docker:

1. Build the Docker image: `./scripts/build.sh`
2. Run the Docker container: `./scripts/run.sh`

## Testing

Run tests using pytest: `pytest tests/`

## License

MIT License
