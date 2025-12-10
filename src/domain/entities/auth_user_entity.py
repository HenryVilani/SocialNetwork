
from dataclasses import dataclass
from src.domain.entities.user_entity import UserRole

@dataclass
class AuthUser:
    """
    Domain entity representing an AuthUser with basic informations.
    
    :param id: Id of the user.
    :type id: str
    :param role: Role of the user.
    :type role: UserRole    
    """

    id: str
    role: UserRole
