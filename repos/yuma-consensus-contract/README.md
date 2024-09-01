
# Yuma Consensus Smart Contract

This repository contains a smart contract implementation of the Yuma consensus mechanism, featuring stake-based reward distribution with an anti-cabal mechanism.

## Features

- Stake-based participation
- Reward distribution based on stake
- Anti-cabal mechanism to prevent centralization
- Simple validator selection process

## Setup

1. Clone this repository
2. Install dependencies (requires Node.js and npm):
   ```
   npm install
   ```
3. Compile the contract:
   ```
   npx hardhat compile
   ```
4. Run tests:
   ```
   npx hardhat test
   ```

## Contract Structure

- `YumaConsensus.sol`: Main contract implementing the Yuma consensus mechanism
- `IYumaConsensus.sol`: Interface for the Yuma consensus contract

## Docker

To build and run the project using Docker, use the scripts in the `scripts` folder:

- `build.sh`: Builds the Docker image
- `run.sh`: Runs the Docker container

## License

This project is licensed under the MIT License.
