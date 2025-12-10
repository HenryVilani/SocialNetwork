
from uuid import UUID
from attrs import define

from src.application.dtos.channel_use_case_dto import GetChannelUseCaseDTO
from src.application.errors.channel_erros import ChannelNotFoundError
from src.application.errors.common_errors import ValueParserError
from src.domain.entities.channel_entity import Channel
from src.domain.repositories.channel_repository import IChannelRepository


@define
class GetChannelUseCase:
    """
    Application use case for retrieve channel by id.
    
    :param channel_repository: Channel repository abstraction.
    :type channel_repository: IChannelRepository
    """
    
    channel_repository: IChannelRepository
    
    def execute(self, channel_id: str) -> Channel:
        """
        Retrieve channel by id.
        
        :param channel_id: Id of channel used to retrieve.
        :type channel_id: str
        :raises ChannelNotFoundError: If channel not found.
        :return: Channel entity
        :rtype: Channel
        """
        
        channel = self.channel_repository.find_by_id(channel_id)
        if channel is None: raise ChannelNotFoundError
        
        return channel
    
        
        