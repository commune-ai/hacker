
import time
import random
import numpy as np
from web3 import Web3
from eth_account import Account

# Connect to Ethereum network (replace with your provider URL)
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR-PROJECT-ID'))

# Contract ABI and address (replace with your deployed contract details)
contract_abi = [...]  # Add your contract ABI here
contract_address = '0x...'  # Add your deployed contract address here

# Load contract
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Miner's Ethereum account (replace with your account details)
miner_private_key = 'YOUR_PRIVATE_KEY'
miner_account = Account.from_key(miner_private_key)

def matrix_multiplication():
    # Simulating matrix multiplication work
    matrix_a = np.random.rand(100, 100)
    matrix_b = np.random.rand(100, 100)
    result = np.dot(matrix_a, matrix_b)
    return Web3.keccak(text=str(result))

def submit_work(work_hash):
    nonce = w3.eth.get_transaction_count(miner_account.address)
    
    # Prepare transaction
    txn = contract.functions.submitWork(work_hash, b'').build_transaction({
        'from': miner_account.address,
        'nonce': nonce,
    })
    
    # Sign and send transaction
    signed_txn = w3.eth.account.sign_transaction(txn, miner_private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    
    # Wait for transaction receipt
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_receipt

def main():
    while True:
        work_hash = matrix_multiplication()
        try:
            receipt = submit_work(work_hash)
            print(f"Work submitted. Transaction hash: {receipt['transactionHash'].hex()}")
        except Exception as e:
            print(f"Error submitting work: {e}")
        
        # Wait before next submission
        time.sleep(random.randint(60, 300))  # Wait 1-5 minutes

if __name__ == "__main__":
    main()
