
from attrs import define
from src.domain.entities.user_entity import User
from src.domain.repositories.user_repository import IUserRepository

@define
class GetUserUseCase:

    user_repository: IUserRepository

    def execute(self, user_id: str) -> User | None:
        
        return self.user_repository.find_by_id(user_id)

