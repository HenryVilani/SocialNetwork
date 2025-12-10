from attrs import define

from src.application.errors.post_errors import PostNotFoundError
from src.domain.entities.post_entity import Post
from src.domain.repositories.post_repository import IPostRepository


@define
class GetPostUseCase:
    """
    Application use case responsible for retrieving a single post.

    :param post_repository: Repository abstraction for post persistence.
    :type post_repository: IPostRepository
    """

    post_repository: IPostRepository

    def execute(self, post_id: str) -> Post:
        """
        Retrieve a post by its identifier.

        :param post_id: Identifier of the post to retrieve.
        :type post_id: str
        :raises PostNotFoundError: If the post cannot be found.
        :return: Post entity instance.
        :rtype: Post
        """
        post = self.post_repository.find_by_id(post_id)
        if post is None: raise PostNotFoundError

        return post
