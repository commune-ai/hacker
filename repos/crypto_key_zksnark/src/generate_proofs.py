
import ezkl
from cryptography.hazmat.primitives.asymmetric import ec, rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os

def generate_eth_key():
    return ec.generate_private_key(ec.SECP256K1(), default_backend())

def generate_polkadot_key():
    return ec.generate_private_key(ec.SECP256R1(), default_backend())

def generate_solana_key():
    return ec.generate_private_key(ec.Ed25519(), default_backend())

def generate_bitcoin_key():
    return ec.generate_private_key(ec.SECP256K1(), default_backend())

def generate_proof(circuit_path, private_key):
    # Convert private key to bytes
    private_key_bytes = private_key.private_bytes(
        encoding=ezkl.Encoding.Raw,
        format=ezkl.PrivateFormat.Raw,
        encryption_algorithm=ezkl.NoEncryption()
    )

    # Generate proof using ezkl
    proof = ezkl.prove(circuit_path, private_key_bytes)
    return proof

def main():
    circuits = {
        "ethereum": "circuits/ethereum_circuit.json",
        "polkadot": "circuits/polkadot_circuit.json",
        "solana": "circuits/solana_circuit.json",
        "bitcoin": "circuits/bitcoin_circuit.json"
    }

    for crypto, circuit_path in circuits.items():
        print(f"Generating proof for {crypto}...")
        if crypto == "ethereum":
            key = generate_eth_key()
        elif crypto == "polkadot":
            key = generate_polkadot_key()
        elif crypto == "solana":
            key = generate_solana_key()
        elif crypto == "bitcoin":
            key = generate_bitcoin_key()

        proof = generate_proof(circuit_path, key)
        
        # Save proof to file
        with open(f"proofs/{crypto}_proof.json", "w") as f:
            f.write(proof)
        
        print(f"Proof for {crypto} generated and saved.")

if __name__ == "__main__":
    main()
