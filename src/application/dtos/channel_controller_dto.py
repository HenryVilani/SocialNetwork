
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class CreateChannelControllerInDTO(BaseModel):

    name: str
    description: str

class CreateChannelControllerOutDTO(BaseModel):
    
    id: str
    
    name: str
    description: str
    
    posts: int
    
    created_at: datetime

class DeleteChannelControllerOutDTO(BaseModel):
    
    status: str

class ChannelDTO(BaseModel):
    
    id: str
    
    name: str
    description: str
    
    posts: int
    
    created_at: datetime

class SearchChannelControllerOutDTO(BaseModel):
    
    channels: List[ChannelDTO]
    next_segment: Optional[int]

class GetChannelControllerOutDTO(BaseModel):
    
    id: str
    
    name: str
    description: str
    
    posts: int
    
    created_at: datetime
    
    
    