
# Yuma Consensus Proof of Stake Distribution System

This repository contains a smart contract implementation of a proof of stake distribution system using Yuma consensus. The system includes miners, validators, admins, and a modular consensus mechanism.

## Features

- Proof of stake distribution of incentives
- Yuma consensus mechanism (replaceable by admin)
- Miner rewards for matrix multiplication
- Validator dividends from voting
- Admin controls for blacklisting miners and updating subnet parameters
- Python validator and miner implementations
- Web3 key verification

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Deploy the smart contract to your preferred Ethereum network.

3. Run the miner:
   ```
   python scripts/miner.py
   ```

4. Run the validator:
   ```
   python scripts/validator.py
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

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
