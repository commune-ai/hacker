
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from eth_account.messages import encode_defunct
from eth_account import Account
import time

app = FastAPI()

class Transaction(BaseModel):
    function_name: str
    cost: float
    timestamp: int
    parameters: dict
    signature: str

class Rollup:
    def __init__(self):
        self.transactions = []
        self.total_cost = 0

    def add_transaction(self, tx):
        self.transactions.append(tx)
        self.total_cost += tx.cost

rollup = Rollup()

@app.post("/execute")
async def execute_transaction(tx: Transaction):
    # Verify the signature
    message = f"{tx.function_name}{tx.cost}{tx.timestamp}{tx.parameters}"
    message_hash = encode_defunct(text=message)
    signer = Account.recover_message(message_hash, signature=tx.signature)
    
    # Here you would typically check if the signer is authorized
    
    # Execute the function (simulated here)
    print(f"Executing {tx.function_name} with parameters {tx.parameters}")
    
    # Add to rollup
    rollup.add_transaction(tx)
    
    return {"status": "success", "message": "Transaction executed and added to rollup"}

@app.get("/rollup")
async def get_rollup():
    return {"transactions": rollup.transactions, "total_cost": rollup.total_cost}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
