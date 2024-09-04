
# PyTorch Inference Rollup Prover

This project demonstrates how to prove a PyTorch inference as an optimistic rollup and post it on an EVM smart contract. The system allows for verification of the inference and includes a slashing mechanism for incorrect proofs.

## Features

- PyTorch model inference
- Optimistic rollup proof generation
- EVM smart contract for proof verification
- Slashing mechanism for incorrect proofs

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/your-username/pytorch-inference-rollup-prover.git
   cd pytorch-inference-rollup-prover
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

1. Perform inference and generate proof:
   ```
   python src/inference.py
   ```

2. Submit proof to the smart contract:
   ```
   python src/submit_proof.py
   ```

3. Verify proof on-chain:
   ```
   python src/verify_proof.py
   ```

## Testing

Run the test suite:
```
pytest tests/
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
