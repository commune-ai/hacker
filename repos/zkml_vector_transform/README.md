
# ZKML Vector Transform

This project implements a Zero-Knowledge Machine Learning (ZKML) framework for proving many-to-one vector transformations using EZKL. It provides a simple class for verifying matrix multiplications in a zero-knowledge setting.

## Requirements

- Python 3.8+
- Docker

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/zkml_vector_transform.git
   cd zkml_vector_transform
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

Inside the Docker container, you can use the `ZKVectorTransform` class to perform and prove vector transformations:

```python
from zkml_vector_transform import ZKVectorTransform

# Create an instance with 3 input vectors of dimension 4
transformer = ZKVectorTransform(num_vectors=3, vector_dim=4)

# Define input vectors
input_vectors = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Perform the transformation and generate a proof
result, proof = transformer.transform_and_prove(input_vectors)

# Verify the proof
is_valid = transformer.verify(input_vectors, result, proof)
print(f"Proof is valid: {is_valid}")
```

## Running Tests

To run the tests, use the following command inside the Docker container:

```
pytest tests/
```

## License

This project is licensed under the MIT License.
