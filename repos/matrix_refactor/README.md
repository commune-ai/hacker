
# Matrix Refactor

A Python library that refactors matrices in Hugging Face models into decompositions that keep the top N ranks.

## Installation

```bash
pip install matrix_refactor
```

## Usage

```python
from matrix_refactor import refactor_matrix

# Load your Hugging Face model
model = ...

# Refactor a specific matrix in the model
refactored_matrix = refactor_matrix(model.some_layer.weight, top_n=10)

# Update the model with the refactored matrix
model.some_layer.weight.data = refactored_matrix
```

## Development

To set up the development environment:

```bash
./scripts/build.sh
```

To run the tests:

```bash
./scripts/run.sh
```

## License

MIT License
