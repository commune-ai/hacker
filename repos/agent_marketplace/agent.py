
from pydantic import BaseModel, Schema
from typing import Callable, Any

class Agent(BaseModel):
    name: str
    description: str
    forward_function: Callable
    schema: dict

    def forward(self, *args, **kwargs) -> Any:
        return self.forward_function(*args, **kwargs)

    class Config:
        arbitrary_types_allowed = True
