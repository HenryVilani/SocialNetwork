

from dataclasses import dataclass
from typing import List, Optional

from src.domain.entities.user_entity import User, UserRole
from src.domain.value_object.email_value_object import Email
from src.domain.value_object.password_value_object import Password
from src.domain.value_object.username_value_object import Username


@dataclass
class CreateUserRepoInDTO:

    role: UserRole

    username: Username
    email: Email
    password: Password

@dataclass
class UpdateUserRepoInDTO:

    role: Optional[UserRole]

    username: Optional[Username]
    email: Optional[Email]
    password: Optional[Password]

@dataclass
class SegmentUserRepoOutDTO:
    users: List[User]
    next_segment: Optional[int]