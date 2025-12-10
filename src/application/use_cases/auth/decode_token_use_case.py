
from attrs import define
from src.domain.entities.auth_user_entity import AuthUser
from src.domain.repositories.auth_repository import IAuthRepository

@define
class DecodeTokenUseCase:
    """
    Application use case for decode token to AuthUser.
    
    :param auth_repository: Auth repository abstraction.
    :type auth_repository: IAuthRepository
    """

    auth_repository: IAuthRepository

    def execute(self, token: str) -> AuthUser:
        """
        Decode token to basic user information (AuthUser)
        
        :param token: Token used to decode.
        :type token: str
        :return: basic user information
        :rtype: AuthUser
        """

        return self.auth_repository.decode_token(token)
