
from pydantic import BaseModel

class Agent(BaseModel):
    id: int
    name: str
    description: str
    price: float
    rating: float
