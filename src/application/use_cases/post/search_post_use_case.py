
from typing import List

from attrs import define
from src.application.dtos.post_repo_dto import SegmentPostRepoOutDTO
from src.domain.entities.post_entity import Post
from src.domain.repositories.post_repository import IPostRepository

@define
class SearchPostUseCase:

    post_repository: IPostRepository

    def execute(self, title: str, length: int, segment: int) -> SegmentPostRepoOutDTO:
        return self.post_repository.find_all_by_title(title, length, segment)

