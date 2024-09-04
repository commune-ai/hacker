
import argparse
from crypto_zksnark import EthereumProver, PolkadotProver, SolanaProver, BitcoinProver

def main():
    parser = argparse.ArgumentParser(description="Crypto zkSNARK Prover")
    parser.add_argument("--crypto", choices=["ethereum", "polkadot", "solana", "bitcoin"], required=True, help="Cryptocurrency type")
    parser.add_argument("--address", required=True, help="Public address")
    parser.add_argument("--private_key", required=True, help="Private key")
    args = parser.parse_args()

    prover_map = {
        "ethereum": EthereumProver,
        "polkadot": PolkadotProver,
        "solana": SolanaProver,
        "bitcoin": BitcoinProver
    }

    prover_class = prover_map[args.crypto]
    prover = prover_class(args.address, args.private_key)
    proof = prover.generate_proof()
    
    print(f"Proof generated for {args.crypto.capitalize()} address: {args.address}")
    print(f"Proof: {proof}")

if __name__ == "__main__":
    main()
