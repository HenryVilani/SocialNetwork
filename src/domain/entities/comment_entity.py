
from abc import ABC
from datetime import datetime


class Comment(ABC):

    id: str
    user_id: str
    post_id: str

    content: str

    created_at: datetime

