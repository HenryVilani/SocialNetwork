
from dataclasses import dataclass
from datetime import datetime
from re import S
from typing import List, Optional

from src.domain.entities.channel_entity import Channel

@dataclass
class CreateChannelUseCaseDTO:
    
    id: str
    
    name: str
    description: str
    
    posts: int
    
    created_at: datetime

@dataclass
class GetChannelUseCaseDTO:
    
    id: str
    
    name: str
    description: str
    
    posts: int
    
    created_at: datetime

@dataclass
class SearchChannelUseCaseDTO:
    
    channels: List[Channel]
    next_segment: Optional[int]