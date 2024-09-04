
import json
from web3 import Web3

def submit_proof():
    # Load proof
    with open('proof.json', 'r') as f:
        proof = json.load(f)

    # Connect to Ethereum network
    w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR-PROJECT-ID'))

    # Contract ABI and address
    contract_abi = [{"inputs":[{"internalType":"bytes","name":"proof","type":"bytes"}],"name":"submitProof","outputs":[],"stateMutability":"nonpayable","type":"function"}]
    contract_address = '0x1234567890123456789012345678901234567890'

    # Create contract instance
    contract = w3.eth.contract(address=contract_address, abi=contract_abi)

    # Prepare transaction
    account = w3.eth.account.from_key('YOUR-PRIVATE-KEY')
    nonce = w3.eth.get_transaction_count(account.address)
    
    # Encode proof
    encoded_proof = Web3.to_hex(Web3.to_bytes(text=json.dumps(proof)))

    # Build transaction
    txn = contract.functions.submitProof(encoded_proof).build_transaction({
        'from': account.address,
        'nonce': nonce,
        'gas': 2000000,
        'gasPrice': w3.eth.gas_price
    })

    # Sign and send transaction
    signed_txn = account.sign_transaction(txn)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

    # Wait for transaction receipt
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    print(f"Proof submitted. Transaction hash: {tx_hash.hex()}")

if __name__ == "__main__":
    submit_proof()
