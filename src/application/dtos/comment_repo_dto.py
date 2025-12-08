

from dataclasses import dataclass
from typing import List, Optional

from src.domain.entities.comment_entity import Comment

@dataclass
class CreateCommentRepoInDTO:

    user_id: str
    post_id: str

    content: str

@dataclass
class SegmentCommentRepoOutDTO:
    
    comments: List[Comment]
    next_segment: Optional[int]

@dataclass
class ErrorOutDTO:

    status: str
