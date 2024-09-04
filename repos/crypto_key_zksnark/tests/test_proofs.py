
import pytest
from src.generate_proofs import generate_eth_key, generate_polkadot_key, generate_solana_key, generate_bitcoin_key, generate_proof
from src.verify_proofs import verify_proof
import os

@pytest.fixture
def circuit_paths():
    return {
        "ethereum": "circuits/ethereum_circuit.json",
        "polkadot": "circuits/polkadot_circuit.json",
        "solana": "circuits/solana_circuit.json",
        "bitcoin": "circuits/bitcoin_circuit.json"
    }

def test_ethereum_proof(circuit_paths):
    key = generate_eth_key()
    proof = generate_proof(circuit_paths["ethereum"], key)
    assert verify_proof(circuit_paths["ethereum"], proof)

def test_polkadot_proof(circuit_paths):
    key = generate_polkadot_key()
    proof = generate_proof(circuit_paths["polkadot"], key)
    assert verify_proof(circuit_paths["polkadot"], proof)

def test_solana_proof(circuit_paths):
    key = generate_solana_key()
    proof = generate_proof(circuit_paths["solana"], key)
    assert verify_proof(circuit_paths["solana"], proof)

def test_bitcoin_proof(circuit_paths):
    key = generate_bitcoin_key()
    proof = generate_proof(circuit_paths["bitcoin"], key)
    assert verify_proof(circuit_paths["bitcoin"], proof)

def test_invalid_proof(circuit_paths):
    key = generate_eth_key()
    proof = generate_proof(circuit_paths["ethereum"], key)
    assert not verify_proof(circuit_paths["polkadot"], proof)
