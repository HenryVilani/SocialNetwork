
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Comment:

    id: str
    user_id: str
    post_id: str

    content: str

    created_at: datetime

