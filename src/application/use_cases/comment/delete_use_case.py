
from uuid import UUID
from attrs import define

from src.application.errors.comment_errors import CommentNotFoundError
from src.application.errors.common_errors import ValueParserError
from src.application.errors.user_errors import UserNotFound
from src.domain.repositories.comment_repository import ICommentRepository
from src.domain.repositories.user_repository import IUserRepository


@define
class DeleteCommentUseCase:
    """
    Application use case for delete comment.
    
    :param user_repository: User repository abstraction.
    :type user_repository: IUserRepository
    :param comment_repository: Comment repository abstraction.
    :type comment_repository: ICommentRepository
    """
    
    user_repository: IUserRepository
    comment_repository: ICommentRepository
    
    def execute(self, user_id: str, comment_id: str):
        """
        Delete comment by id with user_id verification.
        
        :param user_id: Id of user used to garant permission to delete comment.
        :type user_id: str
        :param comment_id: Id of comment used to delete.
        :type comment_id: str
        :rtype: None
        """        
        
        user = self.user_repository.find_by_id(user_id)
        if user is None: raise UserNotFound
        
        comment = self.comment_repository.find_by_id(comment_id)
        if comment is None: raise CommentNotFoundError
        
        self.comment_repository.delete(comment_id)
