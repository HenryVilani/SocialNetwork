from attrs import define
from src.application.dtos.user_repo_dto import CreateUserRepoInDTO
from src.domain.entities.user_entity import User, UserRole
from src.domain.repositories.user_repository import IUserRepository
from src.domain.value_object.password_value_object import Password
from src.domain.value_object.username_value_object import Username
from src.domain.value_object.email_value_object import Email


@define
class CreateUserUseCase:
    """
    Application use case for creating a new user.

    :param user_repository: User repository abstraction.
    :type user_repository: IUserRepository
    """

    user_repository: IUserRepository

    def execute(self, username: str, email: str, role: UserRole, password: str) -> User:
        """
        Create a new user.

        :param username: User username.
        :type username: Username
        :param email: User email.
        :type email: Email
        :param role: User role (e.g., admin or user).
        :type role: UserRole
        :param password: User password.
        :type password: Password
        :return: Newly created user entity.
        :rtype: User
        """

        return self.user_repository.create(
            CreateUserRepoInDTO(
                role=role,
                username=Username(username),
                email=Email(email),
                password=Password(password)
            )
        )
