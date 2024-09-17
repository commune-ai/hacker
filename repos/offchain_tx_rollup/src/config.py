
import os
from dotenv import load_dotenv

load_dotenv()

INFURA_URL = os.getenv("INFURA_URL")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")
CONTRACT_ABI = [
    {
        "inputs": [
            {"internalType": "bytes32", "name": "merkleRoot", "type": "bytes32"},
            {"internalType": "uint256", "name": "totalCost", "type": "uint256"}
        ],
        "name": "submitRollup",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]
