
from datetime import datetime
from re import S
from typing import List, Optional
from pydantic import BaseModel



class CreateChannelUseCaseDTO(BaseModel):
    
    id: str
    
    name: str
    description: str
    
    posts: int
    
    created_at: datetime

class GetChannelUseCaseDTO(BaseModel):
    
    id: str
    
    name: str
    description: str
    
    posts: int
    
    created_at: datetime

class SearchItemUseCaseDTO(BaseModel):
    
    id: str
    name: str
    description: str
    posts: int
    created_at: datetime
    
class SearchChannelUseCaseDTO(BaseModel):
    
    channels: List[SearchItemUseCaseDTO]
    next_segment: Optional[int]