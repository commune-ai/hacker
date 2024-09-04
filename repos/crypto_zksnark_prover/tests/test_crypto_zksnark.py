
import pytest
from src.crypto_zksnark import EthereumProver, PolkadotProver, SolanaProver, BitcoinProver

@pytest.fixture
def ethereum_data():
    return {
        "address": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e",
        "private_key": "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
    }

@pytest.fixture
def polkadot_data():
    return {
        "address": "5GrwvaEF5zXb26Fz9rcQpDWS57CtERHpNehXCPcNoHGKutQY",
        "private_key": "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
    }

@pytest.fixture
def solana_data():
    return {
        "address": "5U3bH5b6XtG8sqFhXzcD7XPKbCdkgHbGKB8GJxr5XwV3",
        "private_key": "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
    }

@pytest.fixture
def bitcoin_data():
    return {
        "address": "1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2",
        "private_key": "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
    }

def test_ethereum_prover(ethereum_data):
    prover = EthereumProver(ethereum_data["address"], ethereum_data["private_key"])
    proof = prover.generate_proof()
    assert proof is not None

def test_polkadot_prover(polkadot_data):
    prover = PolkadotProver(polkadot_data["address"], polkadot_data["private_key"])
    proof = prover.generate_proof()
    assert proof is not None

def test_solana_prover(solana_data):
    prover = SolanaProver(solana_data["address"], solana_data["private_key"])
    proof = prover.generate_proof()
    assert proof is not None

def test_bitcoin_prover(bitcoin_data):
    prover = BitcoinProver(bitcoin_data["address"], bitcoin_data["private_key"])
    proof = prover.generate_proof()
    assert proof is not None
