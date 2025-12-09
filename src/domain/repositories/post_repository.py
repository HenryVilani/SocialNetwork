
from abc import ABC
from typing import List, Optional

from src.application.dtos.post_repo_dto import CreatePostRepoInDTO, SegmentPostRepoOutDTO
from src.domain.entities.post_entity import Post


class IPostRepository(ABC):
    """
    Repository interface for post persistence operations.
    """

    def create(self, post: CreatePostRepoInDTO) -> Post:
        """
        Create a new Post.
        
        :param post: Input data for post creation.
        :type post: CreatePostRepoInDTO
        :return: Created post entity.
        :rtype: Post
        """
        ...

    def delete(self, id: str) -> None:
        """
        Delete a post by id.
        
        :param id: Id of the post to delete.
        :type id: str
        :rtype: None
        """
        ...

    def delete_all_by_user(self, user_id: str) -> None:
        """
        Delete all posts associated with a specific user.
        
        :param user_id: Id of the user whose posts must be deleted.
        :type user_id: str
        :rtype: None
        """
        ...

    def find_by_id(self, id: str) -> Optional[Post]:
        """
        Retrieve a post by id.
        
        :param id: Id of the post to retrieve.
        :type id: str
        :return: Post entity if found; otherwise None.
        :rtype: Optional[Post]
        """
        ...

    def find_all_by_title(self, title: str, length: int, segment: int) -> SegmentPostRepoOutDTO:
        """
        Retrieve posts filtered by title with pagination support.
        
        :param title: Title filter for the query.
        :type title: str
        :param length: Maximum number of items to return.
        :type length: int
        :param segment: Pagination segment (offset).
        :type segment: int
        :return: Result set containing posts and pagination metadata.
        :rtype: SegmentPostRepoOutDTO
        """
        ...

    def find_all_by_user(self, user_id: str, length: int, segment: int) -> SegmentPostRepoOutDTO:
        """
        Retrieve posts associated with a specific user with pagination support.
        
        :param user_id: User id to which posts are associated.
        :type user_id: str
        :param length: Maximum number of items to return.
        :type length: int
        :param segment: Pagination segment (offset).
        :type segment: int
        :return: Result set containing posts and pagination metadata.
        :rtype: SegmentPostRepoOutDTO
        """
        ...


