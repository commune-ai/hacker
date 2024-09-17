
from fastapi import FastAPI, HTTPException
from eth_account.messages import encode_defunct
from web3.auto import w3
import time

app = FastAPI()

transactions = []

@app.post("/submit_transaction")
async def submit_transaction(function_name: str, cost: float, params: str, signature: str):
    message = f"{function_name}:{cost}:{time.time()}:{params}"
    encoded_message = encode_defunct(text=message)
    
    try:
        signer = w3.eth.account.recover_message(encoded_message, signature=signature)
    except:
        raise HTTPException(status_code=400, detail="Invalid signature")
    
    transactions.append({
        "signer": signer,
        "function_name": function_name,
        "cost": cost,
        "params": params,
        "timestamp": time.time()
    })
    
    return {"status": "Transaction recorded"}

@app.get("/get_rollup")
async def get_rollup():
    total_cost = sum(tx["cost"] for tx in transactions)
    return {
        "transactions": transactions,
        "total_cost": total_cost
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
