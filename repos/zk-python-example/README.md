
# ZK Python Example

This repository contains a simple implementation of a Zero-Knowledge Proof system in Python. It demonstrates how a prover can convince a verifier that they know a secret without revealing the secret itself.

## Structure

- `zk_proof/`: Main package containing the ZK proof implementation
  - `__init__.py`: Package initialization
  - `prover.py`: Prover implementation
  - `verifier.py`: Verifier implementation
  - `utils.py`: Utility functions
- `main.py`: Example usage of the ZK proof system
- `scripts/`: Docker-related scripts
  - `build.sh`: Script to build the Docker image
  - `run.sh`: Script to run the Docker container
- `Dockerfile`: Docker configuration file
- `requirements.txt`: Python dependencies

## Usage

To run the example locally:

1. Install the requirements: `pip install -r requirements.txt`
2. Run the main script: `python main.py`

To run using Docker:

1. Build the Docker image: `./scripts/build.sh`
2. Run the Docker container: `./scripts/run.sh`

## How it works

This example implements a simple ZK proof where the prover demonstrates knowledge of a secret number without revealing it. The proof is based on the discrete logarithm problem.

1. The prover generates a commitment based on their secret.
2. The verifier sends a challenge.
3. The prover computes a response based on the secret and challenge.
4. The verifier checks if the response is valid without learning the secret.

For more details, check the implementation in the `zk_proof/` directory.
