
from dataclasses import dataclass
from typing import List, Optional

from src.domain.entities.comment_entity import Comment


@dataclass
class ListCommentUseCaseOutDTO:
    
    comments: List[Comment]
    next_segment: Optional[int]
