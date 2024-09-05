
import uvicorn
from fastapi import FastAPI
from app.routers import agents, users, transactions

app = FastAPI(title="Agent Marketplace")

app.include_router(agents.router)
app.include_router(users.router)
app.include_router(transactions.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
