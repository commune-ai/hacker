
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

# Database connection
conn = psycopg2.connect(
    dbname="usdt_tracker",
    user="postgres",
    password="password",
    host="db",
    port="5432"
)

class Account(BaseModel):
    id: str
    usdt_amount: float

@app.get("/accounts")
def get_accounts():
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("SELECT * FROM accounts")
        return cur.fetchall()

@app.get("/accounts/{account_id}")
def get_account(account_id: str):
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("SELECT * FROM accounts WHERE id = %s", (account_id,))
        account = cur.fetchone()
        if account is None:
            raise HTTPException(status_code=404, detail="Account not found")
        return account

@app.post("/accounts")
def create_account(account: Account):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO accounts (id, usdt_amount) VALUES (%s, %s)",
            (account.id, account.usdt_amount)
        )
        conn.commit()
    return {"message": "Account created successfully"}

@app.put("/accounts/{account_id}")
def update_account(account_id: str, account: Account):
    with conn.cursor() as cur:
        cur.execute(
            "UPDATE accounts SET usdt_amount = %s WHERE id = %s",
            (account.usdt_amount, account_id)
        )
        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="Account not found")
        conn.commit()
    return {"message": "Account updated successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
