
from web3 import Web3
from config import INFURA_URL, CONTRACT_ADDRESS, CONTRACT_ABI

w3 = Web3(Web3.HTTPProvider(INFURA_URL))

def submit_rollup(transactions, total_cost):
    contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)
    
    # Prepare transaction data
    tx_hashes = [Web3.keccak(text=str(tx)) for tx in transactions]
    merkle_root = Web3.keccak(b''.join(tx_hashes))
    
    # Submit to blockchain
    tx = contract.functions.submitRollup(merkle_root, total_cost).buildTransaction({
        'from': w3.eth.accounts[0],
        'nonce': w3.eth.getTransactionCount(w3.eth.accounts[0]),
    })
    
    signed_tx = w3.eth.account.signTransaction(tx, private_key="YOUR_PRIVATE_KEY")
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    
    return w3.toHex(tx_hash)

if __name__ == "__main__":
    # Example usage
    transactions = [...]  # Get from server
    total_cost = sum(tx["cost"] for tx in transactions)
    tx_hash = submit_rollup(transactions, total_cost)
    print(f"Rollup submitted. Transaction hash: {tx_hash}")
