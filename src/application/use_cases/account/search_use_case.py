
from attrs import define

from src.application.dtos.user_repo_dto import SegmentUserRepoOutDTO
from src.application.dtos.user_use_case_dto import SearchUserUseCaseOutDTO
from src.domain.repositories.user_repository import IUserRepository


@define
class SearchUserUseCase:
    """
    Application use case for serach user by username.
    
    :param user_repository: User repository abstraction.
    :type user_repository: IUserRepository
    """
    
    user_repository: IUserRepository
    
    def execute(self, query: str, length: int, segment: int) -> SearchUserUseCaseOutDTO:
        """
        Search user by username and return with pagination support.
        
        :param query: Username query used to search.
        :type query: str
        :param length: Maximum number of items to return.
        :type length: int
        :param segment: Pagination segment (offset).
        :type segment: int
        :return: Result set containing users and pagination metadata.
        :rtype: SearchUserUseCaseOutDTO
        """        
        
        users_segment = self.user_repository.find_all_by_username(query, length, segment)
        
        return SearchUserUseCaseOutDTO(
            users=users_segment.users,
            next_segment=users_segment.next_segment
        )
        
