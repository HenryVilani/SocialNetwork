
from abc import ABC
from typing import List, Optional

from src.application.dtos.user_repo_dto import CreateUserRepoInDTO, SegmentUserRepoOutDTO, UpdateUserRepoInDTO
from src.domain.entities.user_entity import User
from src.domain.value_object.email_value_object import Email


class IUserRepository(ABC):
    """
    Repository interface for user persistent operations.
    """

    def create(self, user: CreateUserRepoInDTO) -> User:
        """
        Create a new user.
        
        :param user: Input data for user creation.
        :type user: CreateUserRepoInDTO
        :return: Description
        :rtype: User
        """
        ...

    def update(self, user_id: str, user: UpdateUserRepoInDTO) -> User:
        """
        Update a user by id.
        
        :param user_id: Id of the user to update.
        :type user_id: str
        :param user: Input data to update user.
        :type user: UpdateUserRepoInDTO
        :return: Updated user entity.
        :rtype: User
        """
        ...

    def delete(self, user_id: str) -> None:
        """
        Delete a user by id.
        
        :param user_id: Id of the user to delete.
        :type user_id: str
        :rtype: None
        """
        ...

    def find_by_id(self, user_id: str) -> Optional[User]:
        """
        Retrieve user by id.
        
        :param user_id: Id of the user to retrieve.
        :type user_id: str
        :return: User entity if found; otherwise None.
        :rtype: Optional[User]
        """
        ...

    def find_all_by_username(self, username: str, length: int, segment: int) -> SegmentUserRepoOutDTO:
        """
        Retrieve all users by username with pagination support.
        
        :param username: Username filter for the query
        :type username: str
        :param length: Maximum number of items to return.
        :type length: int
        :param segment: Pagination segment (offset).
        :type segment: int
        :return: Result set containing users and pagination metadata.
        :rtype: SegmentUserRepoOutDTO
        """
        ...

    def find_by_email(self, email: Email) -> Optional[User]:
        """
        Retrieve user by email.
        
        :param email: Email of the user to retrieve.
        :type email: Email
        :return: User entity if found; otherwise None.
        :rtype: Optional[User]
        """
        ...
