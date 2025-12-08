
from attrs import define
from src.domain.repositories.channel_repository import IChannelRepository
from src.domain.repositories.comment_repository import ICommentRepository
from src.domain.repositories.post_repository import IPostRepository
from src.domain.repositories.user_repository import IUserRepository

@define
class DeleteUserUseCase:
    
    user_repository: IUserRepository
    post_repository: IPostRepository
    comment_repository: ICommentRepository
    channel_repository: IChannelRepository

    def execute(self, user_id: str) -> None:
        
        self.comment_repository.delete_all_by_user(user_id)
        self.post_repository.delete_all_by_user(user_id)
        self.channel_repository.delete_all_by_user(user_id)
        
        self.user_repository.delete(user_id)
        
