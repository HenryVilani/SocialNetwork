
from attrs import define
from src.application.errors.auth_errors import WrongCredentialsError
from src.domain.entities.auth_user_entity import AuthUser
from src.domain.repositories.auth_repository import IAuthRepository
from src.domain.repositories.user_repository import IUserRepository
from src.domain.value_object.email_value_object import Email
from src.domain.value_object.password_value_object import Password

@define
class LoginUserUseCase:

    auth_repository: IAuthRepository
    user_repository: IUserRepository

    def execute(self, email: str, password: str) -> str:

        user = self.user_repository.find_by_email(Email(email))
    
        print("password: ", user.password)
        print("Password: ", Password(password).value)

        if Password.verify(user.password, password):
            return self.auth_repository.generate_token(AuthUser(
                id=user.id,
                role=user.role
            ))

        else:
            raise WrongCredentialsError

        