from attrs import define
from src.application.dtos.post_use_case_dto import SearchPostUseCaseOutDTO
from src.domain.repositories.post_repository import IPostRepository


@define
class SearchPostUseCase:
    """
    Application use case responsible for searching posts by title.

    :param post_repository: Repository abstraction for post persistence.
    :type post_repository: IPostRepository
    """

    post_repository: IPostRepository

    def execute(self, title: str, length: int, segment: int) -> SearchPostUseCaseOutDTO:
        """
        Search posts by title with pagination support.

        The search is performed using the repository, which returns a
        paginated segment. The results are then mapped to output DTOs.

        :param title: Title or partial title to filter posts.
        :type title: str
        :param length: Maximum number of items to return.
        :type length: int
        :param segment: Pagination segment (offset).
        :type segment: int
        :return: Result set containing posts and pagination metadata.
        :rtype: SearchPostUseCaseOutDTO
        """

        posts_segment = self.post_repository.find_all_by_title(title, length, segment)

        return SearchPostUseCaseOutDTO(
            posts=posts_segment.posts,
            next_segment=posts_segment.next_segment
        )
