
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List
from web3 import Web3

app = FastAPI()

# Initialize Web3
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

# In-memory storage for wallets and transactions
wallets: Dict[str, float] = {}
spending_sheet: List[Dict[str, str]] = []

class Transaction(BaseModel):
    from_address: str
    amount: float
    currency: str

class Agent:
    def __init__(self, call_cost: float):
        self.call_cost = call_cost

    def generate(self, prompt: str) -> str:
        # Deduct the call cost
        if self.call_cost > 0:
            # Implement logic to deduct call_cost from user's balance
            pass
        
        # Placeholder for generation logic
        return f"Generated response for: {prompt}"

@app.post("/transaction")
async def record_transaction(transaction: Transaction):
    if transaction.currency not in ["ETH", "USDT", "USDC"]:
        raise HTTPException(status_code=400, detail="Unsupported currency")

    # Convert to USD (simplified conversion)
    usd_amount = transaction.amount
    if transaction.currency == "ETH":
        eth_price = w3.eth.get_price()
        usd_amount = transaction.amount * eth_price

    # Record transaction
    if transaction.from_address in wallets:
        wallets[transaction.from_address] += usd_amount
    else:
        wallets[transaction.from_address] = usd_amount

    # Update spending sheet
    spending_sheet.append({
        "wallet": transaction.from_address,
        "amount": str(usd_amount),
        "currency": "USD"
    })

    return {"status": "Transaction recorded"}

@app.get("/wallets")
async def get_wallets():
    return wallets

@app.get("/spending_sheet")
async def get_spending_sheet():
    return spending_sheet

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
