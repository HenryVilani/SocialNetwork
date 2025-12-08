
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

@dataclass()
class Post:

    id: str
    user_id: str

    channel_id: Optional[str]

    # TODO: add multiple post types

    title: str
    content: str

    tags: List[str]

    created_at: datetime

