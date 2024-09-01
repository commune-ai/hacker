
# Solana-Ethereum Bridge

This project implements a bridge between Solana and Ethereum blockchains using HTTP servers in Python. It includes a multisig system for transaction signing, where each agent is staked and can be slashed if found to be malicious on either Ethereum or Solana.

## Features

- Bidirectional asset transfer between Solana and Ethereum
- Multisig transaction signing
- Staking mechanism for validators
- Slashing mechanism for malicious behavior
- HTTP server implementation in Python

## Setup

1. Install Docker and Docker Compose
2. Clone this repository
3. Run `./scripts/build.sh` to build the Docker environment
4. Run `./scripts/run.sh` to start the bridge servers

## Architecture

The bridge consists of multiple components:
- Solana listener
- Ethereum listener
- Bridge server
- Multisig server
- Staking contract (on both Solana and Ethereum)

For more details, see the `docs` folder.

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
