
from typing import List, Optional

from attrs import define

from src.application.dtos.post_repo_dto import CreatePostRepoInDTO
from src.domain.entities.post_entity import Post
from src.domain.repositories.post_repository import IPostRepository

@define
class CreatePostUseCase:

    post_repository: IPostRepository

    def execute(self,
        user_id: str,
        title: str,
        content: str,
        tags: List[str],
        channel_id: Optional[str]
    ) -> Post:
        
        post = self.post_repository.create(
            CreatePostRepoInDTO(
                user_id=user_id,
                title=title,
                content=content,
                tags=tags,
                channel_id=channel_id
            )
        )

        return post

