
from web3 import Web3
from solcx import compile_standard
import json

def deploy_contract():
    # Connect to local testnet
    w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

    # Compile the contract
    with open('contracts/RateLimiter.sol', 'r') as file:
        contract_source_code = file.read()

    compiled_sol = compile_standard({
        "language": "Solidity",
        "sources": {
            "RateLimiter.sol": {
                "content": contract_source_code
            }
        },
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
                }
            }
        }
    })

    # Extract the contract data
    contract_data = compiled_sol['contracts']['RateLimiter.sol']['RateLimiter']
    bytecode = contract_data['evm']['bytecode']['object']
    abi = json.loads(contract_data['metadata'])['output']['abi']

    # Deploy the contract
    RateLimiter = w3.eth.contract(abi=abi, bytecode=bytecode)
    tx_hash = RateLimiter.constructor().transact()
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    print(f"Contract deployed at address: {tx_receipt.contractAddress}")
    return tx_receipt.contractAddress

if __name__ == "__main__":
    deploy_contract()
