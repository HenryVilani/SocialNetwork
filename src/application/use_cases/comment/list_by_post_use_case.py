
from attrs import define

from src.application.dtos.comment_repo_dto import SegmentCommentRepoOutDTO
from src.application.dtos.comment_use_case_dto import ListCommentUseCaseOutDTO
from src.application.errors.post_errors import PostNotFoundError
from src.domain.repositories.comment_repository import ICommentRepository
from src.domain.repositories.post_repository import IPostRepository


@define
class ListCommentByPostUseCase:
    """
    Application use case for list comments by post.
    
    :param post_repository: Post repository abstraction.
    :type post_repository: IPostRepository
    :param comment_repository: Comment repository abstraction.
    :type comment_repository: ICommentRepository
    """
    
    post_repository: IPostRepository
    comment_repository: ICommentRepository
    
    def execute(self, post_id: str, length: int, segment: int) -> ListCommentUseCaseOutDTO:
        """
        List comments by post id with pagination support.
        
        :param post_id: Id of post used to list comments.
        :type post_id: str
        :param length: Maximum number of items to return.
        :type length: int
        :param segment: Pagination segment (offset).
        :type segment: int
        :return: Result set containing comments and pagination metadata.
        :rtype: ListCommentUseCaseOutDTO
        """
        
        post = self.post_repository.find_by_id(post_id)
        if post is None: raise PostNotFoundError
        
        comments_segment = self.comment_repository.find_all_by_post(post_id, length, segment)
        
        return ListCommentUseCaseOutDTO(
            comments=comments_segment.comments,
            next_segment=comments_segment.next_segment
        )
        
