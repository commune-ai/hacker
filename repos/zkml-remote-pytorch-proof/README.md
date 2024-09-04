
# zkML Remote PyTorch Proof

This repository demonstrates a proof-of-concept implementation of running a PyTorch model remotely using Zero-Knowledge Machine Learning (zkML) techniques. The goal is to allow Billy to run a model without revealing the model weights.

## Features

- Remote PyTorch model execution
- Zero-knowledge proofs for model integrity
- Secure input and output handling
- Docker-based deployment

## Prerequisites

- Docker
- Python 3.8+
- PyTorch
- zkML libraries (simulated in this PoC)

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/your-username/zkml-remote-pytorch-proof.git
   cd zkml-remote-pytorch-proof
   ```

2. Build the Docker image:
   ```
   ./scripts/build.sh
   ```

3. Run the Docker container:
   ```
   ./scripts/run.sh
   ```

## Usage

1. Prepare your input data in the `data/input.json` file.
2. Run the remote model execution:
   ```
   python src/remote_execution.py
   ```
3. Check the output in the `data/output.json` file.

## Testing

Run the test suite:
```
pytest tests/
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

