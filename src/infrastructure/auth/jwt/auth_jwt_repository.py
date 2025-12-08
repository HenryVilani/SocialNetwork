
import os
import jwt
from src.application.errors.auth_errors import PayloadParserError
from src.domain.entities.auth_user_entity import AuthUser
from src.domain.repositories.auth_repository import IAuthRepository
from src.infrastructure.auth.jwt.auth_dto import AuthPayloadDTO


class AuthJWTRepository(IAuthRepository):

    def generate_token(self, user: AuthUser):
        
        payload = AuthPayloadDTO(
            user_id=user.id,
            role=user.role.value
        )
        return jwt.encode(payload.model_dump(), os.getenv("AUTH_SECRET"), algorithm="HS256")
    
    def decode_token(self, token) -> AuthUser:
        
        raw_payload = jwt.decode(token, os.getenv("AUTH_SECRET"), algorithms=["HS256"])
        try:

            payload = AuthPayloadDTO(**raw_payload)
            return AuthUser(
                id=payload.user_id,
                role=payload.role
            )
        except:
            raise PayloadParserError


