
from dataclasses import dataclass
from typing import List, Optional

from src.domain.entities.post_entity import Post


@dataclass
class CreatePostRepoInDTO:

    user_id: str
    
    channel_id: Optional[str]

    title: str
    content: str

    tags: List[str]

@dataclass
class SegmentPostRepoOutDTO:
    
    posts: List[Post]
    next_segment: Optional[int]
