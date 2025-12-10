

from dataclasses import dataclass
from typing import List, Optional

from src.domain.entities.user_entity import User

@dataclass
class SearchUserUseCaseOutDTO:
    users: List[User]
    next_segment: Optional[int]
