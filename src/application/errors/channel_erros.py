
from src.application.errors.base_errors import BaseError


class ChannelNotFoundError(BaseError):

    def __init__(self):
        super().__init__("channel_not_found")

class ChannelNameAlreadyExistsError(BaseError):
    
    def __init__(self):
        super().__init__("channel_name_already_exists")
