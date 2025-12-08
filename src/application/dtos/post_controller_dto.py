
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class CreatePostControllerInDTO(BaseModel):
    
    title: str
    content: str
    
    tags: List[str]
    
    channel_id: Optional[str]
    
class CreatePostControllerOutDTO(BaseModel):
    
    id: str
    title: str
    content: str
    
    tags: List[str]
    
    channel_id: Optional[str]
    
    created_at: datetime
    
class GetPostControllerOutDTO(BaseModel):
    
    id: str
    title: str
    content: str
    
    tags: List[str]
    
    created_at: datetime
    
class DeletePostControllerOutDTO(BaseModel):
    
    status: str
    
class SearchPostControllerOutDTO(BaseModel):
    
    posts: List[GetPostControllerOutDTO]
    
    next_segment: Optional[int]
    