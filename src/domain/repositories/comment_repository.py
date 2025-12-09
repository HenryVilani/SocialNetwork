
from abc import ABC
from typing import Optional

from src.application.dtos.comment_repo_dto import CreateCommentRepoInDTO, SegmentCommentRepoOutDTO
from src.domain.entities.comment_entity import Comment

class ICommentRepository(ABC):
    """
    Repository interface for comment persistent operations.
    """

    def create(self, comment: CreateCommentRepoInDTO) -> Comment:
        """
        Create a new comment.
        
        :param comment: Input data for comment creation.
        :type comment: CreateCommentRepoInDTO
        :return: Created comment entity
        :rtype: Comment
        """
        ...
    
    def delete(self, comment_id: str) -> None:
        """
        Delete a comment by id.

        :param comment_id: Id of the comment to delete.
        :type comment_id: str
        :rtype: None
        """
        ...
    
    def delete_all_by_user(self, user_id: str) -> None: 
        """
        Delte all comment associated with a specific user.
        
        :param user_id: User id whose comments should be deleted.
        :type user_id: str
        :rtype: None
        """
        ...

    def find_all_by_post(self, post_id: str, length: int, segment: int) -> SegmentCommentRepoOutDTO: 
        """
        Retrieve comments by a post with pagination support.
        
        :param post_id: Id of the post associated with comments.
        :type post_id: str
        :param length: Maximum number of items to return.
        :type length: int
        :param segment: Pagination segment (offset).
        :type segment: int
        :return: Result set containing comments and pagination metadata.
        :rtype: SegmentCommentRepoOutDTO
        """
        ...

    def find_all_by_user(self, user_id: str, length: int, segment: int) -> SegmentCommentRepoOutDTO:
        """
        Retrieve comments associated with a specific user with pagination support.
        
        :param user_id: User id to which comments are associated.
        :type user_id: str
        :param length: Maximum number of items to return.
        :type length: int
        :param segment: Pagination segment (offset).
        :type segment: int
        :return: Result set containing comments and pagination metadata.
        :rtype: SegmentCommentRepoOutDTO
        """
        ...
    
    def find_by_id(self, comment_id: str) -> Optional[Comment]:
        """
        Retrieve a comment by id.
        
        :param comment_id: Id of the comment to retrieve.
        :type comment_id: str
        :return: Comment entity if found; otherwise None.
        :rtype: Optional[Channel]
        """
        ...
