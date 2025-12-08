
from uuid import UUID
from attrs import define

from src.application.errors.comment_errors import CommentNotFoundError
from src.application.errors.common_errors import ValueParserError
from src.application.errors.user_errors import UserNotFound
from src.domain.repositories.comment_repository import ICommentRepository
from src.domain.repositories.user_repository import IUserRepository


@define
class DeleteCommentUseCase:
    
    user_repository: IUserRepository
    comment_repository: ICommentRepository
    
    def execute(self, user_id: str, comment_id: str):
        
        try:
            UUID(user_id)
            UUID(comment_id)
        except:
            raise ValueParserError
        
        user = self.user_repository.find_by_id(user_id)
        if user is None: raise UserNotFound
        
        comment = self.comment_repository.find_by_id(comment_id)
        if comment is None: raise CommentNotFoundError
        
        self.comment_repository.delete(comment_id)
