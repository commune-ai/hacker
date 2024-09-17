
# Off-chain Transaction Rollup with On-chain Verification

This project implements an off-chain transaction rollup system with on-chain verification for smart contract interactions. It allows clients to sign transactions off-chain, which are then verified and rolled up before being submitted to the blockchain for cost expensing.

## Features

- Off-chain transaction signing
- Server-side transaction verification
- Transaction rollup
- On-chain proof submission
- Smart contract for expense verification

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Set up your Ethereum node or Infura endpoint in `config.py`.

3. Deploy the smart contract using `scripts/deploy_contract.py`.

4. Run the server:
   ```
   python src/server.py
   ```

5. Use the client to submit transactions:
   ```
   python src/client.py
   ```

## Testing

Run tests using pytest:
```
pytest tests/
```

## Docker

Build the Docker image:
```
./scripts/build.sh
```

Run the Docker container:
```
./scripts/run.sh
```

## License

MIT License
