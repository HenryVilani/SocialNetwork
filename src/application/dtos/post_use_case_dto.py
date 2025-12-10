

from dataclasses import dataclass
from typing import List, Optional

from src.domain.entities.post_entity import Post

@dataclass
class SearchPostUseCaseOutDTO:
    
    posts: List[Post]
    next_segment: Optional[int]


@dataclass
class GetPostByUserUseCaseOutDTO:
    posts: List[Post]
    next_segment: Optional[int]
    