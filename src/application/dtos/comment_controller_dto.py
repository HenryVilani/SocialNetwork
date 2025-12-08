
from typing import List, Optional
from pydantic import BaseModel

from src.domain.entities.comment_entity import Comment

class CreateCommentControllerInDTO(BaseModel):
    
    content: str

class CreateCommentControllerOutDTO(BaseModel):
    
    id: str
    content: str

class ListCommentByPostControllerOutDTO(BaseModel):
    
    comments: List[Comment]
    next_segment: Optional[int]

class DeleteCommentControllerOutDTO(BaseModel):
    status: str