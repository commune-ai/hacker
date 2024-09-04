
# ZKML Vector Transformation Framework

This project implements a Zero-Knowledge Machine Learning (ZKML) framework in Python that proves a many-to-one vector transformation. It uses EZKL (Easy Zero-Knowledge Learning) to generate and verify proofs for the transformation of M vectors of dimension N into a single resulting vector of dimension N.

## Features

- Implementation of many-to-one vector transformation
- ZKML proof generation and verification using EZKL
- Docker support for easy setup and execution
- Pytest suite for testing the implementation

## Requirements

- Python 3.8+
- Docker
- EZKL

## Quick Start

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/zkml_vector_transform.git
   cd zkml_vector_transform
   ```

2. Build the Docker image:
   ```
   ./scripts/build.sh
   ```

3. Run the application:
   ```
   ./scripts/run.sh
   ```

4. Run tests:
   ```
   ./scripts/run.sh pytest
   ```

## Project Structure

- `src/`: Source code for the ZKML framework
- `tests/`: Pytest test suite
- `scripts/`: Docker build and run scripts
- `Dockerfile`: Docker configuration

## License

This project is licensed under the MIT License. See the LICENSE file for details.

