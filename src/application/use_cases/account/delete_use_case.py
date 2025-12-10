
from attrs import define
from src.domain.repositories.channel_repository import IChannelRepository
from src.domain.repositories.comment_repository import ICommentRepository
from src.domain.repositories.post_repository import IPostRepository
from src.domain.repositories.user_repository import IUserRepository

@define
class DeleteUserUseCase:
    """
    Application use case for deleting a user.
    
    :param user_repository: User repository abstraction.
    :type user_repository: IUserRepository
    :param post_repository: Post repository abstraction.
    :type post_repository: IPostRepository
    :param comment_repository: Comment repository abstraction.
    :type comment_repository: ICommentRepository
    :param channel_repository: Channel repository abstraction.
    """
    
    user_repository: IUserRepository
    post_repository: IPostRepository
    comment_repository: ICommentRepository
    channel_repository: IChannelRepository

    def execute(self, user_id: str) -> None:
        """
        Delete a user by id.
        
        :param user_id: Id associated with a user to delete.
        :type user_id: str
        :rtype: None
        """
        
        self.comment_repository.delete_all_by_user(user_id)
        self.post_repository.delete_all_by_user(user_id)
        self.channel_repository.delete_all_by_user(user_id)
        
        self.user_repository.delete(user_id)
        
