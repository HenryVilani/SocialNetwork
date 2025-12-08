
from attrs import define

from src.application.errors.post_errors import PostNotFoundError
from src.domain.entities.post_entity import Post
from src.domain.repositories.post_repository import IPostRepository


@define
class GetPostUseCase:
    
    post_repository: IPostRepository
    
    def execute(self, post_id: str) -> Post:
        
        post = self.post_repository.find_by_id(post_id)
        if post is None: raise PostNotFoundError
        
        return post
        
