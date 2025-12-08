
from src.application.errors.base_errors import BaseError

class UserAlreadyExists(BaseError):

    def __init__(self):
        super().__init__("user_already_exists")

class UserNotFound(BaseError):

    def __init__(self):
        super().__init__("user_not_found")

class UsernameInvalid(BaseError):

    def __init__(self):
        super().__init__("username_invalid")

class EmailInvalid(BaseError):

    def __init__(self):
        super().__init__("email_invalid")

class PasswordInvalid(BaseError):

    def __init__(self):
        super().__init__("password_invalid")