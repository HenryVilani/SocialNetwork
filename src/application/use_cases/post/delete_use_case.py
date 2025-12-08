

from attrs import define
from src.application.errors.auth_errors import UnauthorizedAction
from src.application.errors.post_errors import PostNotFoundError
from src.domain.repositories.post_repository import IPostRepository

@define
class DeletePostUseCase:

    post_repository: IPostRepository

    def execute(self, user_id: str, post_id: str):

        post = self.post_repository.find_by_id(post_id)
        if post is None: raise PostNotFoundError
        
        print("POST USER ID: ", post.user_id)
        print("USER ID: ", user_id)
        if post.user_id != user_id: raise UnauthorizedAction

        self.post_repository.delete(post_id)


