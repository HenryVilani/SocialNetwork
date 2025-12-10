

from dataclasses import dataclass
from typing import List, Optional

from pydantic import BaseModel


class SegmentUserUseCaseOutDTO(BaseModel):
    users: List[User]
    next_segment: Optional[int]
