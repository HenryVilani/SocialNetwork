
from pydantic import BaseModel


class ErrorControllerOutDTO(BaseModel):
    
    status: str
