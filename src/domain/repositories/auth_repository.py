
from abc import ABC
from src.domain.entities.auth_user_entity import AuthUser


class IAuthRepository(ABC):

    def generate_token(self, user: AuthUser) -> str: ...
    def decode_token(self, token: str) -> AuthUser: ...
