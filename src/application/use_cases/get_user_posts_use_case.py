
from src.domain.repositories.post_repository import IPostRepository


class GetUserPostsUseCase:

    post_repository: IPostRepository

    def __init__(self, post_repository: IPostRepository):
        self.post_repository = post_repository

    async def execute(self, user_id: str, length: int, segment: int):
        return await self.post_repository.find_all_by_user(user_id)

