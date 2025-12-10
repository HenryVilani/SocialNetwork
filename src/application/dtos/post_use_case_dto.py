

from typing import List, Optional
from pydantic import BaseModel

class SearchPostItemDTO(BaseModel):
    
    user_id: str
    channel_id: Optional[str]
    title: str
    content: str
    
    tags: List[str]

class SearchPostUseCaseOutDTO(BaseModel):
    
    posts: List[SearchPostItemDTO]
    next_segment: Optional[int]


class GetPostByUserPostItemDTO(BaseModel):
    
    user_id: str
    channel_id: Optional[str]
    title: str
    content: str
    
    tags: List[str]

class GetPostByUserUseCaseOutDTO(BaseModel):
    posts: List[GetPostByUserPostItemDTO]
    next_segment: Optional[int]
    