
# ZKML Vector Transformation

This repository contains a Zero-Knowledge Machine Learning (ZKML) framework that proves a many-to-one vector transformation using EZKL. The transformation takes M vectors of dimension N and produces a resulting vector of dimension N.

## Requirements

- Python 3.8+
- Docker

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/your-username/zkml-vector-transformation.git
   cd zkml-vector-transformation
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

Once inside the Docker container, you can run the main script:

```
python src/main.py
```

This will generate the proof for the vector transformation and verify it.

## Testing

To run the tests, execute:

```
pytest tests/
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
