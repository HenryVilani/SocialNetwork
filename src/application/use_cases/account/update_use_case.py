
from attrs import define
from src.application.dtos.user_repo_dto import UpdateUserRepoInDTO
from src.domain.entities.user_entity import User
from src.domain.repositories.user_repository import IUserRepository
from src.domain.value_object.email_value_object import Email
from src.domain.value_object.password_value_object import Password
from src.domain.value_object.username_value_object import Username

@define
class UpdateUserUseCase:

    user_repository: IUserRepository

    def execute(
        self, 
        user_id: str,
        username: str | None = None,
        email: str | None = None,
        password: str | None = None,
        role: str | None = None
    ) -> User:
        
        dto = UpdateUserRepoInDTO(
            role=role,
            username=Username(username),
            email=Email(email),
            password=Password(password)
        )

        return self.user_repository.update(user_id, dto)

