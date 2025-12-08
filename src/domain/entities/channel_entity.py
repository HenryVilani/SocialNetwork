

from abc import ABC
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Channel:

    id: str

    user_id: str

    name: str

    description: str

    posts: int

    created_at: datetime