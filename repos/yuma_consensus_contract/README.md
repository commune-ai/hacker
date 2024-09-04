
# Yuma Consensus Smart Contract

This repository contains a smart contract implementation for a proof of stake distribution system based on the Yuma consensus mechanism. The contract includes functionality for miners, validators, admins, and a modular consensus mechanism.

## Features

- Modular consensus mechanism (replaceable by admin)
- Miner and validator roles
- Admin controls for blacklisting miners and updating subnet parameters
- Token distribution for matrix multiplication tasks
- Python validator and miner scripts
- Web3 key verification

## Structure

- `contracts/`: Contains the Solidity smart contract
- `scripts/`: Contains build and run scripts for Docker environment
- `python/`: Contains Python scripts for validator and miner

## Setup

1. Clone the repository
2. Run `./scripts/build.sh` to build the Docker environment
3. Run `./scripts/run.sh` to run the environment in Docker

## Usage

Refer to the individual script files for usage instructions.

