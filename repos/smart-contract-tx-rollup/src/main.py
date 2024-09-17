
import os
from web3 import Web3
from dotenv import load_dotenv
from rollup import TxRollup

load_dotenv()

def main():
    # Connect to Ethereum network
    w3 = Web3(Web3.HTTPProvider(os.getenv('ETHEREUM_RPC_URL')))
    
    # Load contract ABI and address
    with open('contract_abi.json', 'r') as abi_file:
        contract_abi = abi_file.read()
    contract_address = os.getenv('CONTRACT_ADDRESS')
    
    # Initialize contract
    contract = w3.eth.contract(address=contract_address, abi=contract_abi)
    
    # Initialize rollup
    rollup = TxRollup(w3, contract)
    
    # Fetch and rollup transactions
    rollup.fetch_approved_transactions()
    rollup.aggregate_transactions()
    rollup.submit_rollup()

if __name__ == "__main__":
    main()
