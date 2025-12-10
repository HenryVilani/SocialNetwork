
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

@dataclass()
class Post:
    """
    Domain entity representing a Post.
    
    :param id: Id of the post.
    :type id: str
    :param user_id: User id associated with the post.
    :type user_id: str
    :param title: Title of the post.
    :type title: str
    :param content: Content of the post.
    :type content: str
    :param tags: List of tags of the post.
    :type tags: List[str]
    :param created_at: Datetime of post creation.
    :type created_at: datetime
    """    

    id: str
    user_id: str
    channel_id: Optional[str]

    # TODO: add multiple post types

    title: str
    content: str
    tags: List[str]
    created_at: datetime

