
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Comment:
    """
    Domain entity representing a Comment.
    
    :param id: Id of the Comment.
    :type id: str
    :param user_id: Id of the user associated with a comment.
    :type user_id: str
    :param post_id: Id of the post associated with a comment.
    :type post_id: str
    :param content: Content of the comment.
    :type content: str
    :param created_at: Datetime of comment creation.
    :type created_at: datetime 
    """

    id: str
    user_id: str
    post_id: str
    content: str
    created_at: datetime

