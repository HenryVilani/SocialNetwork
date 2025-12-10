
from typing import List, Optional

from attrs import define

from src.application.dtos.post_repo_dto import CreatePostRepoInDTO
from src.domain.entities.post_entity import Post
from src.domain.repositories.post_repository import IPostRepository

@define
class CreatePostUseCase:
    """
    Application use case for creating a new post.

    :param post_repository: Repository abstraction for post persistence.
    :type post_repository: IPostRepository
    """

    post_repository: IPostRepository

    def execute(self,
        user_id: str,
        title: str,
        content: str,
        tags: List[str],
        channel_id: Optional[str]
    ) -> Post:
        """
        Execute the post creation and return post created.

        :param user_id: Identifier of the post author.
        :type user_id: str
        :param title: Title of the post.
        :type title: str
        :param content: Content of the post.
        :type content: str
        :param tags: List of tags associated with the post.
        :type tags: List[str]
        :param channel_id: Optional channel identifier where the post 
            will be published.
        :type channel_id: Optional[str]
        :return: Post entity created.
        :rtype: Post
        """
        
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

