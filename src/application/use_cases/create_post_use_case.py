
from typing import List

from src.application.dtos.post_repo_dto import CreatePostRepoInDTO
from src.domain.entities.post_entity import Post
from src.domain.repositories.post_repository import IPostRepository


class CreatePostUseCase:

    post_repository: IPostRepository

    def __init__(self, post_repository: IPostRepository):
        self.post_repository = post_repository

    async def execute(self,
        user_id: str,
        title: str,
        content: str,
        tags: List[str]
    ) -> Post:
        
        post = await self.post_repository.create(
            CreatePostRepoInDTO(
                user_id,
                title,
                content,
                tags
            )
        )

        return post

