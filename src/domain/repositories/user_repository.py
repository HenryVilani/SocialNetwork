
from abc import ABC
from typing import List

from src.domain.entities.user_entity import User


class IUserRepository(ABC):

    async def create(self) -> User: ...

    async def update(self) -> User: ...

    async def delete(self) -> None: ...

    async def find_by_id(self, user_id: str) -> User | None: ...

    async def find_all_by_name(self, name: str) -> List[User]: ...
    
