
# Python Zero-Knowledge Proof Example

This repository contains a simple example of a Zero-Knowledge Proof (ZKP) implementation in Python using the `zkp` library. The example demonstrates how to prove knowledge of a secret number without revealing the number itself.

## Requirements

- Python 3.7+
- Docker (for running in a containerized environment)

## Project Structure

- `src/`: Contains the main Python script
- `scripts/`: Contains build and run scripts for Docker
- `requirements.txt`: Lists the Python dependencies

## Running the Example

### Using Docker

1. Build the Docker image:
   ```
   ./scripts/build.sh
   ```

2. Run the example in a Docker container:
   ```
   ./scripts/run.sh
   ```

### Without Docker

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the example:
   ```
   python src/zk_example.py
   ```

## How it Works

The example uses the Schnorr protocol to prove knowledge of a discrete logarithm. The prover demonstrates knowledge of a secret number `x` such that `y = g^x mod p`, where `g` and `p` are public parameters.

1. The prover generates a random number `r` and computes `t = g^r mod p`.
2. The verifier sends a random challenge `c`.
3. The prover computes the response `s = r + c * x mod (p-1)`.
4. The verifier checks if `g^s == t * y^c mod p`.

If the check passes, the verifier is convinced that the prover knows `x` without learning its value.

