

from typing import List, Optional
from pydantic import BaseModel

from src.domain.entities.post_entity import Post

class SearchPostUseCaseOutDTO(BaseModel):
    
    posts: List[Post]
    next_segment: Optional[int]


class GetPostByUserUseCaseOutDTO(BaseModel):
    posts: List[Post]
    next_segment: Optional[int]
    