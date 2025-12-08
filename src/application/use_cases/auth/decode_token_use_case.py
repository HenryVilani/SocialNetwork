
from attrs import define
from src.domain.entities.auth_user_entity import AuthUser
from src.domain.repositories.auth_repository import IAuthRepository

@define
class DecodeTokenUseCase:

    auth_repository: IAuthRepository

    def execute(self, token: str) -> AuthUser:

        return self.auth_repository.decode_token(token)
