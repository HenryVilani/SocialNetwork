
from attrs import define

from src.application.dtos.channel_repo_dto import SegmentChannelRepoOutDTO
from src.domain.repositories.channel_repository import IChannelRepository


@define
class SearchChannelUseCase:
    
    channel_repository: IChannelRepository
    
    def execute(self, query: str, length: int, segment: int) -> SegmentChannelRepoOutDTO:
        
        return self.channel_repository.find_all_by_name(query, length, segment)

