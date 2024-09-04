
# Crypto zkSNARK Prover

This project implements a Zero-Knowledge Succinct Non-Interactive Argument of Knowledge (zkSNARK) using ezkl to prove the possession of a valid private key corresponding to a public key (address) for various cryptocurrencies without revealing the private key.

Supported cryptocurrencies:
- Ethereum
- Polkadot
- Solana
- Bitcoin

## Prerequisites

- Docker
- Python 3.8+
- ezkl

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/your-username/crypto_zksnark_prover.git
   cd crypto_zksnark_prover
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

Inside the Docker container, you can run the zkSNARK prover for different cryptocurrencies:

```
python src/main.py --crypto <ethereum|polkadot|solana|bitcoin> --address <public_address> --private_key <private_key>
```

This will generate a proof that you possess the private key corresponding to the given public address without revealing the private key itself.

## Testing

To run the tests:

```
pytest tests/
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
