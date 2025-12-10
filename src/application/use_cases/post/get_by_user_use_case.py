from attrs import define
from src.application.dtos.post_use_case_dto import GetPostByUserUseCaseOutDTO, GetPostByUserPostItemDTO
from src.domain.repositories.post_repository import IPostRepository


@define
class GetUserPostsUseCase:
    """
    Application use case responsible for retrieving posts created by a user.

    :param post_repository: Repository abstraction for post persistence.
    :type post_repository: IPostRepository
    """

    post_repository: IPostRepository

    def execute(self, user_id: str, length: int, segment: int) -> GetPostByUserUseCaseOutDTO:
        """
        Retrieve posts belonging to a specific user.

        :param user_id: Identifier of the user whose posts will be fetched.
        :type user_id: str
        :param length: Maximum number of items to return.
        :type length: int
        :param segment: Pagination segment (offset).
        :type segment: int
        :return: Result set containing posts and pagination metadata.
        :rtype: GetPostByUserSegmentUseCaseOutDTO
        """
        posts_segment = self.post_repository.find_all_by_user(user_id, length, segment)
        
        return GetPostByUserUseCaseOutDTO(
            posts=posts_segment.posts,
            next_segment=posts_segment.next_segment
        )
