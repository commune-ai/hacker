
# Off-chain Rollup Verifier

This project implements an off-chain verification system with on-chain rollup for tracking and expensing client-server interactions. It allows clients to sign transactions for off-chain server function calls and provides a mechanism to post proof of these interactions on-chain as a rollup.

## Features

- Client-side transaction signing
- Server-side verification of signed transactions
- On-chain rollup of transaction proofs
- Batch processing of off-chain interactions
- Cost tracking and on-chain expensing

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your Ethereum node or provider
4. Configure the smart contract address in `config.py`

## Usage

1. Run the client: `python client.py`
2. Run the server: `python server.py`
3. Execute the rollup: `python rollup.py`

## Testing

Run tests using pytest: `pytest tests/`

## Docker

Build the Docker image: `./scripts/build.sh`
Run the Docker container: `./scripts/run.sh`

## License

MIT License
