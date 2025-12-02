
from abc import ABC
from typing import List

from src.application.dtos.comment_repo_dto import CreateCommentRepoInDTO
from src.domain.entities.comment_entity import Comment

class ICommentRepository(ABC):

    async def create(self, comment: CreateCommentRepoInDTO): ...
    
    async def delete(self, user_id: str, comment_id: str): ...

    async def find_all(self, length: int, segment: int) -> List[Comment]: ...
