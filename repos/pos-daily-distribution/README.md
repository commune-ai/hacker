
# POS Daily Distribution Smart Contract

This repository contains a smart contract implementation for a Proof-of-Stake (PoS) system with daily token distribution. The system includes validator registration, voting mechanics, and daily emission distribution based on stake and votes.

## Features

- ERC20 token for staking and rewards
- Validator registration
- Daily emission distribution
- Voting mechanism for reward allocation
- Miner and validator roles

## Smart Contracts

- `POSToken.sol`: ERC20 token implementation
- `StakingContract.sol`: Main contract for staking, validation, and distribution

## Setup and Deployment

1. Install dependencies:
   ```
   npm install
   ```

2. Compile contracts:
   ```
   npx hardhat compile
   ```

3. Deploy contracts:
   ```
   npx hardhat run scripts/deploy.js --network <your-network>
   ```

4. Run tests:
   ```
   npx hardhat test
   ```

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

This project is licensed under the MIT License.
