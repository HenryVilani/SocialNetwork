
from dataclasses import dataclass
from enum import Enum
from src.domain.value_object.email_value_object import Email
from src.domain.value_object.password_value_object import Password
from src.domain.value_object.username_value_object import Username

class UserRole(str, Enum):
    ADMIN="admin"
    USER="user"

@dataclass
class User:

    id: str
    username: Username
    email: Email
    role: UserRole
    password: Password
