
# ZKML Vector Transform

This repository contains a simple zkML framework for proving many-to-one vector transformations using EZKL. It provides a class for verifying matrix multiplication in a zero-knowledge setting.

## Requirements

- Python 3.7+
- Docker

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/zkml-vector-transform.git
   cd zkml-vector-transform
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

Inside the Docker container, you can run the main script:

```
python src/main.py
```

This will demonstrate the usage of the `ZKVectorTransform` class for verifying matrix multiplication.

## Testing

To run the tests:

```
pytest tests/
```

## License

This project is licensed under the MIT License.
