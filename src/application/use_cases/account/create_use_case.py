
from attrs import define
from src.application.dtos.user_repo_dto import CreateUserRepoInDTO
from src.domain.entities.user_entity import User, UserRole
from src.domain.repositories.user_repository import IUserRepository
from src.domain.value_object.password_value_object import Password
from src.domain.value_object.username_value_object import Username
from src.domain.value_object.email_value_object import Email


@define
class CreateUserUseCase:

    user_repository: IUserRepository

    def execute(self, username: str, email: str, role: UserRole, password: str) -> User:

        return self.user_repository.create(CreateUserRepoInDTO(
            role=role,
            username=Username(username),
            email=Email(email),
            password=Password(password)
        ))