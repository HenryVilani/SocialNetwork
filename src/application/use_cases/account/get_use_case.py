
from typing import Optional
from attrs import define
from src.domain.entities.user_entity import User
from src.domain.repositories.user_repository import IUserRepository

@define
class GetUserUseCase:
    """
    Application use case for get a user by id.
    
    :param user_repository: User repository abstraction.
    :type user_repository: IUserRepository
    """

    user_repository: IUserRepository

    def execute(self, user_id: str) -> Optional[User]:
        """
        Get a user by id.
        
        :param user_id: Id associated with a user.
        :type user_id: str
        :return: User enttity if found; otherwise None.
        :rtype: Optional[User]
        """
        
        return self.user_repository.find_by_id(user_id)

