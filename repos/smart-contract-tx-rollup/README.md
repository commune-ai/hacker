
# Smart Contract Transaction Rollup

This project implements a rollup mechanism for transactions approved on a smart contract using Python. It aggregates multiple transactions into a single batch, reducing gas costs and improving overall efficiency on the blockchain.

## Features

- Connect to Ethereum network
- Fetch approved transactions from a smart contract
- Aggregate transactions into batches
- Submit rollup transactions to the blockchain
- Test suite for verifying rollup functionality

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/your-username/smart-contract-tx-rollup.git
   cd smart-contract-tx-rollup
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

Once inside the Docker environment, you can run the main script:

```
python src/main.py
```

## Testing

To run the test suite:

```
pytest tests/
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
