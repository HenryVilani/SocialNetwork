

from abc import ABC
from datetime import datetime


class Channel(ABC):

    id: str

    user_id: str

    name: str

    description: str

    posts: int

    created_at: datetime