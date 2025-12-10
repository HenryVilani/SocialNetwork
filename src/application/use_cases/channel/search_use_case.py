
from attrs import define

from src.application.dtos.channel_use_case_dto import SearchChannelUseCaseDTO
from src.domain.repositories.channel_repository import IChannelRepository
from src.domain.repositories.post_repository import IPostRepository


@define
class SearchChannelUseCase:
    """
    Application use case for search channel by name.
    
    :param channel_repository: Channel repository abstraction.
    :type channel_repository: IChannelRepository
    :param post_repository: Post repository abstraction.
    :type post_repository: IPostRepository
    """
    
    channel_repository: IChannelRepository
    post_repository: IPostRepository
    
    def execute(self, query: str, length: int, segment: int) -> SearchChannelUseCaseDTO:
        """
        Search channel by name with pagination support.
        
        :param query: Name of channel used like query.
        :type query: str
        :param length: Maximum number of items to return.
        :type length: int
        :param segment: Pagination segment (offset).
        :type segment: int
        :return: Result set containing channels and pagination metadata.
        :rtype: SearchChannelUseCaseDTO
        """
        
        channel_segment = self.channel_repository.find_all_by_name(query, length, segment)
        
        return SearchChannelUseCaseDTO(
            channels=channel_segment.channels,
            next_segment=channel_segment.next_segment
        )

