
from attrs import define

from src.application.dtos.comment_repo_dto import SegmentCommentRepoOutDTO
from src.application.errors.post_errors import PostNotFoundError
from src.domain.repositories.comment_repository import ICommentRepository
from src.domain.repositories.post_repository import IPostRepository


@define
class ListCommentByPostUseCase:
    
    post_repository: IPostRepository
    comment_repository: ICommentRepository
    
    def execute(self, post_id: str, length: int, segment: int) -> SegmentCommentRepoOutDTO:
        
        post = self.post_repository.find_by_id(post_id)
        if post is None: raise PostNotFoundError
        
        return self.comment_repository.find_all_by_post(post_id, length, segment)
        
