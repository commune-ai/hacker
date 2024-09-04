
# Proof of Stake Emission Contract

This repository contains a smart contract system for an EVM-compatible blockchain that implements a proof-of-stake mechanism with daily emissions, validator registration, miner rewards, and delegated staking.

## Features

- ERC20 token for staking and rewards
- Daily emission distribution based on proof of stake
- Validator and miner roles
- Delegated staking
- Admin-controlled parameter changes

## Smart Contracts

- `Token.sol`: The ERC20 token used for staking and rewards
- `StakingContract.sol`: The main contract handling staking, emissions, and rewards
- `ValidatorRegistry.sol`: Contract for registering and managing validators

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

To build and run the environment using Docker:

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
