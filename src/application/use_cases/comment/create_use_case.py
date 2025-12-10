
from attrs import define

from src.application.dtos.comment_repo_dto import CreateCommentRepoInDTO
from src.application.errors.post_errors import PostNotFoundError
from src.application.errors.user_errors import UserNotFound
from src.domain.repositories.comment_repository import ICommentRepository
from src.domain.repositories.post_repository import IPostRepository
from src.domain.repositories.user_repository import IUserRepository
from src.domain.entities.comment_entity import Comment

@define
class CreateCommentUseCase:
    """
    Application use case for comment creation.
    
    :param post_repository: Post repository abstraction.
    :type post_repository: IPostRepository
    :parm comment_repository: Comment repository abstraction.
    :type comment_repository: ICommentRepository
    :param user_repository: User repository abstraction.
    :type user_repository: IUserRepository
    """
    
    post_repository: IPostRepository
    comment_repository: ICommentRepository
    user_repository: IUserRepository
    
    def execute(self, user_id: str, post_id: str, content: str) -> Comment:
        """
        Create comment by user_id and post_id.
        
        :param user_id: Id of user used to associated comment author.
        :type user_id: str
        :param post_id: Id of post used to associated comment to post.
        :type post_id: str
        :param content: Content of comment.
        :type content: str
        :return: Return comment entity created.
        :rtype: Comment
        """        
        
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
        

    
