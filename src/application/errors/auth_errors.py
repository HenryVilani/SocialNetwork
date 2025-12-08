
from src.application.errors.base_errors import BaseError


class PayloadParserError(BaseError):
    def __init__(self):
        super().__init__("payload_parser_error")

class WrongCredentialsError(BaseError):
    def __init__(self):
        super().__init__("wrong_credentials_error")

class NeedAuthentication(BaseError):
    def __init__(self):
        super().__init__("need_authentication")
        
class UnauthorizedAction(BaseError):
    def __init__(self):
        super().__init__("unauthorized_action")