
from uuid import UUID
from attrs import define

from src.application.dtos.channel_repo_dto import CreateChannelRepoInDTO
from src.application.errors.channel_erros import ChannelNameAlreadyExistsError
from src.application.errors.common_errors import ValueParserError
from src.domain.entities.channel_entity import Channel
from src.domain.repositories.channel_repository import IChannelRepository


@define
class CreateChannelUseCase:
    
    channel_repository: IChannelRepository
    
    def execute(self, user_id: str, name: str, description: str) -> Channel:
        
        try:
            UUID(user_id)
        except:
            raise ValueParserError
        
        segment_channel = self.channel_repository.find_all_by_name(name, 1, 1)
        if len(segment_channel.channels) > 0: raise ChannelNameAlreadyExistsError
        
        channel = self.channel_repository.create(
            CreateChannelRepoInDTO(
                user_id=user_id,
                name=name,
                description=description
            )
        )
        
        return channel
        
