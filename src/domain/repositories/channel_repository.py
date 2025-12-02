
from abc import ABC
from typing import List

from src.application.dtos.channel_repo_dto import CreateChannelRepoInDTO, UpdateChannelRepoInDTO
from src.domain.entities.channel_entity import Channel


class IChannelRepository(ABC):

    async def create(self, channel: CreateChannelRepoInDTO) -> Channel: ...

    async def update(self, user_id: str, channel: UpdateChannelRepoInDTO): ...

    async def delete(self, user_id: str, channel_id: str) -> bool: ...

    async def find_by_id(self, id: str) -> Channel: ...

    async def find_all_by_name(self, name: str, length: int, segment: int) -> List[Channel]: ... 
