
from attrs import define

from src.application.dtos.user_repo_dto import SegmentUserRepoOutDTO
from src.domain.repositories.user_repository import IUserRepository


@define
class SearchUserUseCase:
    
    user_repository: IUserRepository
    
    def execute(self, query: str, length: int, segment: int) -> SegmentUserRepoOutDTO:
        
        return self.user_repository.find_all_by_username(query, length, segment)
