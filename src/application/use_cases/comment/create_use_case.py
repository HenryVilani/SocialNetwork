
from uuid import UUID
from attrs import define

from src.application.dtos.comment_repo_dto import CreateCommentRepoInDTO
from src.application.errors.common_errors import ValueParserError
from src.application.errors.post_errors import PostNotFoundError
from src.application.errors.user_errors import UserNotFound
from src.domain.repositories.comment_repository import ICommentRepository
from src.domain.repositories.post_repository import IPostRepository
from src.domain.repositories.user_repository import IUserRepository


@define
class CreateCommentUseCase:
    
    post_repository: IPostRepository
    comment_repository: ICommentRepository
    user_repository: IUserRepository
    
    def execute(self, user_id: str, post_id: str, content: str):
        
        try:
            UUID(user_id)
            UUID(post_id)
        except:
            raise ValueParserError
        
        user = self.user_repository.find_by_id(user_id)
        if user is None: UserNotFound
        
        post = self.post_repository.find_by_id(post_id)
        if post is None: PostNotFoundError
        
        dto = CreateCommentRepoInDTO(
            user_id=user_id,
            post_id=post_id,
            content=content
        )
        
        return self.comment_repository.create(dto)
        

    
