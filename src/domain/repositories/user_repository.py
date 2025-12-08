
from abc import ABC
from typing import List

from src.application.dtos.user_repo_dto import CreateUserRepoInDTO, SegmentUserRepoOutDTO, UpdateUserRepoInDTO
from src.domain.entities.user_entity import User
from src.domain.value_object.email_value_object import Email


class IUserRepository(ABC):

    def create(self, user: CreateUserRepoInDTO) -> User: ...

    def update(self, user_id: str, user: UpdateUserRepoInDTO) -> User: ...

    def delete(self, user_id: str) -> None: ...

    def find_by_id(self, user_id: str) -> User | None: ...

    def find_all_by_username(self, name: str, length: int, segment: int) -> SegmentUserRepoOutDTO: ...

    def find_by_email(self, email: Email) -> User | None: ...
