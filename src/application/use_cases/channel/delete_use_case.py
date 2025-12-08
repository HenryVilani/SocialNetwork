
from uuid import UUID
from attrs import define

from src.application.errors.auth_errors import UnauthorizedAction
from src.application.errors.channel_erros import ChannelNotFoundError
from src.application.errors.common_errors import ValueParserError
from src.domain.repositories.channel_repository import IChannelRepository


@define
class DeleteChannelUseCase:
    
    channel_repository: IChannelRepository
    
    def execute(self, user_id: str, channel_id: str):
        
        try:
            UUID(channel_id)
            UUID(user_id)
        except:
            raise ValueParserError
        
        channel = self.channel_repository.find_by_id(channel_id)
        if channel is None: raise ChannelNotFoundError
        
        if channel.user_id != user_id: raise UnauthorizedAction
        
        self.channel_repository.delete(channel_id)
