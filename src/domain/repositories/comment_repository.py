
from abc import ABC
from typing import List, Optional

from src.application.dtos.comment_repo_dto import CreateCommentRepoInDTO, SegmentCommentRepoOutDTO
from src.domain.entities.comment_entity import Comment

class ICommentRepository(ABC):

    def create(self, comment: CreateCommentRepoInDTO) -> Comment: ...
    
    def delete(self, comment_id: str) -> None: ...
    
    def delete_all_by_user(self, user_id: str) -> None: ...

    def find_all_by_post(self, post_id: str, length: int, segment: int) -> SegmentCommentRepoOutDTO: ...

    def find_all_by_user(self, user_id: str, length: int, segment: int) -> SegmentCommentRepoOutDTO: ...
    
    def find_by_id(self, comment_id: str) -> Optional[Comment]: ...
