
from web3 import Web3
import time
from config import ETHEREUM_NODE_URL, SMART_CONTRACT_ADDRESS, ROLLUP_BATCH_SIZE, ROLLUP_INTERVAL

w3 = Web3(Web3.HTTPProvider(ETHEREUM_NODE_URL))

# ABI for the smart contract (simplified)
ABI = [
    {
        "inputs": [
            {"type": "address[]", "name": "clients"},
            {"type": "uint256[]", "name": "costs"},
            {"type": "uint256", "name": "timestamp"}
        ],
        "name": "submitRollup",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

contract = w3.eth.contract(address=SMART_CONTRACT_ADDRESS, abi=ABI)

def process_rollup(transactions):
    clients = []
    costs = []
    total_cost = 0

    for tx in transactions:
        if tx['signer'] not in clients:
            clients.append(tx['signer'])
            costs.append(0)
        index = clients.index(tx['signer'])
        costs[index] += tx['cost']
        total_cost += tx['cost']

    timestamp = int(time.time())

    # Submit the rollup to the smart contract
    tx_hash = contract.functions.submitRollup(clients, costs, timestamp).transact()
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    print(f"Rollup submitted. Transaction hash: {tx_hash.hex()}")
    print(f"Total cost: {total_cost}")

    return receipt

def main():
    while True:
        if len(transactions) >= ROLLUP_BATCH_SIZE:
            batch = transactions[:ROLLUP_BATCH_SIZE]
            del transactions[:ROLLUP_BATCH_SIZE]
            process_rollup(batch)
        time.sleep(ROLLUP_INTERVAL)

if __name__ == "__main__":
    main()
