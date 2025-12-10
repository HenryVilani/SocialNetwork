from attrs import define
from src.application.errors.auth_errors import UnauthorizedAction
from src.application.errors.post_errors import PostNotFoundError
from src.domain.repositories.post_repository import IPostRepository


@define
class DeletePostUseCase:
    """
    Application use case responsible for deleting a post.

    :param post_repository: Repository abstraction for post persistence.
    :type post_repository: IPostRepository
    """

    post_repository: IPostRepository

    def execute(self, user_id: str, post_id: str) -> None:
        """
        Execute the deletion of a post.

        Steps performed:

        * Retrieve the post instance by its identifier.
        * Ensure the post exists.
        * Validate that the requesting user is the owner.
        * Delegate deletion to the repository.

        :param user_id: Identifier of the user requesting the deletion.
        :type user_id: str
        :param post_id: Identifier of the post to be deleted.
        :type post_id: str
        :raises PostNotFoundError: If the post does not exist.
        :raises UnauthorizedAction: If the requesting user is not the owner.
        :return: None
        """
        post = self.post_repository.find_by_id(post_id)
        if post is None:
            raise PostNotFoundError

        if post.user_id != user_id:
            raise UnauthorizedAction

        self.post_repository.delete(post_id)
