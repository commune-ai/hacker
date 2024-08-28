
from pydantic import BaseModel
from typing import Callable, Any

class Function(BaseModel):
    name: str
    description: str
    function: Callable
    schema: dict

    def execute(self, *args, **kwargs) -> Any:
        return self.function(*args, **kwargs)

    class Config:
        arbitrary_types_allowed = True
