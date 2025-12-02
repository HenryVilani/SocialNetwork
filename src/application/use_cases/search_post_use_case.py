
from typing import List
from src.domain.entities.post_entity import Post
from src.domain.repositories.post_repository import IPostRepository


class SearchPostUseCase:

    post_repository: IPostRepository

    def __init__(self, post_repository: IPostRepository):
        self.post_repository = post_repository

    async def execute(self, title: str, length: int, segment: int) -> List[Post]:
        return await self.post_repository.find_all_by_title(title, length, segment)

