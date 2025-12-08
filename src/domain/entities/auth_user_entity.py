
from dataclasses import dataclass
from src.domain.entities.user_entity import UserRole

@dataclass
class AuthUser:

    id: str
    role: UserRole
