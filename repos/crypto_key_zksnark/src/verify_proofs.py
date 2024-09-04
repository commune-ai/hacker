
import ezkl
import json

def verify_proof(circuit_path, proof_path):
    with open(proof_path, "r") as f:
        proof = json.load(f)
    
    result = ezkl.verify(circuit_path, proof)
    return result

def main():
    circuits = {
        "ethereum": "circuits/ethereum_circuit.json",
        "polkadot": "circuits/polkadot_circuit.json",
        "solana": "circuits/solana_circuit.json",
        "bitcoin": "circuits/bitcoin_circuit.json"
    }

    for crypto, circuit_path in circuits.items():
        print(f"Verifying proof for {crypto}...")
        proof_path = f"proofs/{crypto}_proof.json"
        
        result = verify_proof(circuit_path, proof_path)
        
        if result:
            print(f"Proof for {crypto} is valid.")
        else:
            print(f"Proof for {crypto} is invalid.")

if __name__ == "__main__":
    main()
