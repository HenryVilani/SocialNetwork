
from attrs import define
from src.domain.repositories.post_repository import IPostRepository

@define
class GetUserPostsUseCase:

    post_repository: IPostRepository

    def execute(self, user_id: str, length: int, segment: int):
        return self.post_repository.find_all_by_user(user_id)

