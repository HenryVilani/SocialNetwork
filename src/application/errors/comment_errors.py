
from src.application.errors.base_errors import BaseError


class CommentNotFoundError(BaseError):
    def __init__(self):
        super().__init__("comment_not_found")
