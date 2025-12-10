

from typing import List, Optional
from pydantic import BaseModel

from src.domain.entities.user_entity import User

class SearchUserUseCaseOutDTO(BaseModel):
    users: List[User]
    next_segment: Optional[int]
