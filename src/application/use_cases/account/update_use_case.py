
from typing import Optional
from attrs import define
from src.application.dtos.user_repo_dto import UpdateUserRepoInDTO
from src.domain.entities.user_entity import User, UserRole
from src.domain.repositories.user_repository import IUserRepository
from src.domain.value_object.email_value_object import Email
from src.domain.value_object.password_value_object import Password
from src.domain.value_object.username_value_object import Username

@define
class UpdateUserUseCase:
    """
    Application use case for update user.
    
    :param user_repository: User repository abstraction.
    :type user_repository: IUserRepository
    """

    user_repository: IUserRepository

    def execute(
        self, 
        user_id: str,
        username: Optional[str] = None,
        email: Optional[str] = None,
        password: Optional[str] = None,
        role: Optional[UserRole] = None
    ) -> User:
        """
        Update user by id.
        
        :param user_id: Id of user used to update.
        :type user_id: str
        :param username: New username used to update.
        :type username: Optional[str]
        :param email: New email used to update.
        :type email: Optional[str]
        :param password: New password to update.
        :type password: Optional[passowrd]
        :param role: New role to update.
        :type role: UserRole
        :return: Updated user entity.
        :rtype: User
        """
        
        dto = UpdateUserRepoInDTO(
            role=role,
            username=Username(username),
            email=Email(email),
            password=Password(password)
        )

        return self.user_repository.update(user_id, dto)

