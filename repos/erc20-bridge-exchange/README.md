
# ERC20 Bridge Exchange

This project implements a bridge for exchanging ERC20 tokens for USDC or USDT. It consists of a smart contract, a Python server, and a Next.js frontend.

## Structure

- `contracts/`: Solidity smart contracts
- `server/`: Python server for handling transactions
- `frontend/`: Next.js frontend application
- `scripts/`: Docker build and run scripts
- `tests/`: PyTest files for testing the server

## Setup

1. Install Docker
2. Run `./scripts/build.sh` to build the Docker environment
3. Run `./scripts/run.sh` to start the application

## Usage

1. Connect your wallet to the frontend
2. Select the ERC20 token you want to receive
3. Choose USDC or USDT for payment
4. Enter the amount and confirm the transaction

## Testing

Run `pytest` in the `tests/` directory to execute the test suite.

## License

MIT
