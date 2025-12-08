
from abc import ABC
from typing import List

from src.application.dtos.post_repo_dto import CreatePostRepoInDTO, SegmentPostRepoOutDTO
from src.domain.entities.post_entity import Post


class IPostRepository(ABC):

    def create(self, post: CreatePostRepoInDTO) -> Post: ...

    def delete(self, id: str) -> None: ...

    def delete_all_by_user(self, user_id: str) -> None: ...

    def find_by_id(self, id: str) -> Post | None: ...

    def find_all_by_title(self, title: str, length: int, segment: int) -> SegmentPostRepoOutDTO: ...

    def find_all_by_user(self, user_id: str, length: int, segment: int) -> SegmentPostRepoOutDTO: ...


