
from abc import ABC
from src.domain.entities.auth_user_entity import AuthUser


class IAuthRepository(ABC):
    """
    Authentication repository for token-based authentication operations
    """
    
    def generate_token(self, user: AuthUser) -> str: 
        """
        Generete a token string with AuthUser
        
        :param user: Simple informations about user
        :type user: AuthUser
        :return: Return token string
        :rtype: str
        """
        ...

    def decode_token(self, token: str) -> AuthUser: 
        """
        Decode token and return AuthUser instance
        
        :param token: Token string
        :type token: str
        :return: Return the AuthUser    
        :rtype: AuthUser    
        """
        ...
