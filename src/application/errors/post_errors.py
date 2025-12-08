
from src.application.errors.base_errors import BaseError


class PostNotFoundError(BaseError):
    def __init__(self):
        super().__init__("post_not_found")
