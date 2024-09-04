
# Crypto Key zk-SNARK Proof

This project implements zk-SNARKs using ezkl to prove the presence of valid private keys for Ethereum, Polkadot, Solana, and Bitcoin without revealing the actual keys.

## Requirements

- Docker
- Python 3.8+
- ezkl

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/your-username/crypto_key_zksnark.git
   cd crypto_key_zksnark
   ```

2. Build the Docker environment:
   ```
   ./scripts/build.sh
   ```

3. Run the Docker environment:
   ```
   ./scripts/run.sh
   ```

## Usage

Inside the Docker container, you can run the following commands:

1. Generate proofs:
   ```
   python src/generate_proofs.py
   ```

2. Verify proofs:
   ```
   python src/verify_proofs.py
   ```

3. Run tests:
   ```
   pytest tests/
   ```

## Project Structure

- `src/`: Contains the main Python scripts
- `scripts/`: Contains Docker build and run scripts
- `tests/`: Contains pytest files
- `circuits/`: Contains the zk-SNARK circuits for each cryptocurrency

## License

This project is licensed under the MIT License.
