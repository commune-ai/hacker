
# Vector Transform ZKP

This project demonstrates a smart contract that verifies the computation of a Python function that transforms a set of vectors into another vector using Zero-Knowledge Proofs (ZKP) via EZKL.

## Overview

The system consists of three main components:
1. A Solidity smart contract for on-chain verification
2. Python code for off-chain vector transformation
3. EZKL integration for generating and verifying zero-knowledge proofs

## Setup

1. Install dependencies:
   ```
   pip install ezkl numpy
   npm install -g truffle
   ```

2. Build the Docker environment:
   ```
   ./scripts/build.sh
   ```

3. Run the environment:
   ```
   ./scripts/run.sh
   ```

## Usage

1. Generate the proof:
   ```
   python scripts/generate_proof.py
   ```

2. Deploy the smart contract:
   ```
   truffle migrate
   ```

3. Verify the proof on-chain:
   ```
   truffle exec scripts/verify_proof.js
   ```

## Project Structure

- `contracts/`: Solidity smart contracts
- `scripts/`: Python and JavaScript scripts for proof generation and verification
- `test/`: Test files for the smart contract
- `migrations/`: Truffle migration files
- `build.sh`: Script to build the Docker environment
- `run.sh`: Script to run the Docker environment

## License

This project is licensed under the MIT License.
