
from dataclasses import dataclass
from enum import Enum
from src.domain.value_object.email_value_object import Email
from src.domain.value_object.password_value_object import Password
from src.domain.value_object.username_value_object import Username

class UserRole(str, Enum):
    """
    Enumeration of user roles.
    
    * ``ADMIN`` - Administrative user with elevated permissions.
    * ``USER`` - Standard user with regular permissions.
    """
    ADMIN="admin"
    USER="user"

@dataclass
class User:
    """
    Domain entity representing an User.
    
    :param id: Id of the user.
    :type id: str
    :param username: User's username value object.
    :type username: Username
    :param email: User's email value object.
    :type email: Email
    :param role: User role classification.
    :type role: UserRole
    :param password: User's password value-object
    :type password: Password
    """

    id: str
    username: Username
    email: Email
    role: UserRole
    password: Password
