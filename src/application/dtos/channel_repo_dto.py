
from dataclasses import dataclass
from typing import List, Optional

from src.domain.entities.channel_entity import Channel


@dataclass
class CreateChannelRepoInDTO:

    user_id: str

    name: str
    description: str

@dataclass
class UpdateChannelRepoInDTO:

    name: Optional[str]
    description: Optional[str]

@dataclass
class SegmentChannelRepoOutDTO:
    
    channels: List[Channel]
    next_segment: Optional[int]

