
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Channel:
    """
    Domain entity representing a Channel.
    
    :param id: Id of the channel.
    :type id: str
    :param user_id: Id of the user associated with a channel.
    :type user_id: str
    :param name: Name of the channel.
    :type name: str
    :param description: Description of the channel.
    :type description: str
    :param posts: Number of posts of channel.
    :type posts: int
    :param created_at: Datetime of channel creation.
    :type created_at: datetime
    """

    id: str
    user_id: str
    name: str
    description: str
    created_at: datetime