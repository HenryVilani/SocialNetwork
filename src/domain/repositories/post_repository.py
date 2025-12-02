
from abc import ABC
from typing import List

from src.application.dtos.post_repo_dto import CreatePostRepoInDTO
from src.domain.entities.post_entity import Post


class IPostRepository(ABC):

    async def create(self, post: CreatePostRepoInDTO) -> Post: ...

    async def delete(self, id: str) -> None: ...

    async def find_by_id(self, id: str) -> Post | None: ...

    async def find_all_by_title(self, title: str, length: int, segment: int) -> List[Post]: ...

    async def find_all_by_user(self, user_id: str, length: int, segment: int) -> List[Post]: ...
