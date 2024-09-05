
from pydantic import BaseModel
from datetime import datetime

class Transaction(BaseModel):
    id: int
    user_id: int
    agent_id: int
    amount: float
    timestamp: datetime
