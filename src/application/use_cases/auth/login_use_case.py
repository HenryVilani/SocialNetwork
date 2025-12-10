
from attrs import define
from src.application.errors.auth_errors import WrongCredentialsError
from src.domain.entities.auth_user_entity import AuthUser
from src.domain.repositories.auth_repository import IAuthRepository
from src.domain.repositories.user_repository import IUserRepository
from src.domain.value_object.email_value_object import Email
from src.domain.value_object.password_value_object import Password

@define
class LoginUserUseCase:
    """
    Application use case for login a user.
    
    :param auth_repository: Auth repository abstraction.
    :type auth_repository: IAuthRepository
    :param user_repository: User repository abstraction.
    :type use_repository: IUserRepository
    """

    auth_repository: IAuthRepository
    user_repository: IUserRepository

    def execute(self, email: str, password: str) -> str:
        """
        Login user with email and password.
        
        :param email: Email used to login user.
        :type email: str
        :param password: Passowrd used to login user.
        :type password: str
        :return: If login correctly return token string
        :rtype: str
        :raises WrongCredentialsError: If email or password is wrong.
        """

        user = self.user_repository.find_by_email(Email(email))

        if Password.verify(user.password, password):
            return self.auth_repository.generate_token(AuthUser(
                id=user.id,
                role=user.role
            ))

        else:
            raise WrongCredentialsError

        