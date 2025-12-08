
from uuid import UUID
from attrs import define

from src.application.errors.channel_erros import ChannelNotFoundError
from src.application.errors.common_errors import ValueParserError
from src.domain.entities.channel_entity import Channel
from src.domain.repositories.channel_repository import IChannelRepository


@define
class GetChannelUseCase:
    
    channel_repository: IChannelRepository
    
    def execute(self, channel_id: str) -> Channel:
        
        try:
            UUID(channel_id)
        except:
            raise ValueParserError
        
        channel = self.channel_repository.find_by_id(channel_id)
        if channel is None: raise ChannelNotFoundError
        
        return channel
    
        
        