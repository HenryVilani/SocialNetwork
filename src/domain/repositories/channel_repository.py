
from abc import ABC
from typing import List, Optional

from src.application.dtos.channel_repo_dto import CreateChannelRepoInDTO, SegmentChannelRepoOutDTO, UpdateChannelRepoInDTO
from src.domain.entities.channel_entity import Channel


class IChannelRepository(ABC):

    def create(self, channel: CreateChannelRepoInDTO) -> Channel: ...

    def update(self, channel_id: str, channel: UpdateChannelRepoInDTO) -> Channel: ...

    def delete(self, channel_id: str) -> None: ...

    def delete_all_by_user(self, user_id: str) -> None: ...

    def find_by_id(self, channel_id: str) -> Optional[Channel]: ...

    def find_all_by_name(self, name: str, length: int, segment: int) -> SegmentChannelRepoOutDTO: ... 
