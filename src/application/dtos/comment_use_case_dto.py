
from typing import List, Optional
from pydantic import BaseModel

from src.domain.entities.comment_entity import Comment


class ListCommentUseCaseOutDTO(BaseModel):
    
    comments: List[Comment]
    next_segment: Optional[int]
