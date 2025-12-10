
from attrs import define

from src.application.dtos.channel_repo_dto import CreateChannelRepoInDTO
from src.application.dtos.channel_use_case_dto import CreateChannelUseCaseDTO
from src.application.errors.channel_erros import ChannelNameAlreadyExistsError
from src.domain.entities.channel_entity import Channel
from src.domain.repositories.channel_repository import IChannelRepository
from src.domain.repositories.post_repository import IPostRepository


@define
class CreateChannelUseCase:
    """
    Application use case for create a channel.
    
    :param channel_repository: Channel repository abstraction.
    :type channel_repository: IChannelRepository
    :param post_repository: Post repository abstraction.
    :type post_repository: IPostRepository
    """
    
    channel_repository: IChannelRepository
    post_repository: IPostRepository
    
    def execute(self, user_id: str, name: str, description: str) -> Channel:
        """
        Create a channel associated with user.
        
        :param user_id: Id of user to used for associate with channel.
        :type user_id: str
        :param name: Name of channel.
        :type name: str
        :param description: Description of channel.
        :type description: str
        :raises ChannelNameAlreadyExistsError: If name of channel already exists.
        :return: Channel entity.
        :rtype: Channel
        """
        
        segment_channel = self.channel_repository.find_all_by_name(name, 1, 1)
        if len(segment_channel.channels) > 0: raise ChannelNameAlreadyExistsError
        
        channel = self.channel_repository.create(
            CreateChannelRepoInDTO(
                user_id=user_id,
                name=name,
                description=description
            )
        )
        
        posts = self.post_repository.count_by_channel(channel.id)
        
        return CreateChannelUseCaseDTO(
            id=channel.id,
            name=channel.name,
            description=channel.description,
            posts=posts,
            created_at=channel.created_at
        )
        
