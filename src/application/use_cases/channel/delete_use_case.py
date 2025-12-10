
from attrs import define

from src.application.errors.auth_errors import UnauthorizedAction
from src.application.errors.channel_erros import ChannelNotFoundError
from src.domain.repositories.channel_repository import IChannelRepository


@define
class DeleteChannelUseCase:
    """
    Application use case for delete channel.
    
    :param channel_repository: Channel repository abstraction.
    :type channel_repository: IChannelRepository
    """
    
    channel_repository: IChannelRepository
    
    def execute(self, user_id: str, channel_id: str):
        """
        Delete a channel by user_id and channel_id.
        
        :param user_id: Id of user used to garant permission to delete channel.
        :type user_id: str
        :param channel_id: Id of channel used to delete.
        :type channel_id: str
        :rtype: None
        """
        
        channel = self.channel_repository.find_by_id(channel_id)
        if channel is None: raise ChannelNotFoundError
        
        if channel.user_id != user_id: raise UnauthorizedAction
        
        self.channel_repository.delete(channel_id)
