
import re
from src.application.errors.user_errors import UsernameInvalid


class Username:

    def __init__(self, username: str):
        self._validate(username)
        self._username = username

    def _validate(self, username: str) -> None:
        if not username or len(username) < 5 or len(username) > 25:
            raise UsernameInvalid()
        
        if not re.match(r'^[a-zA-Z0-9.\-]+$', username):
            raise UsernameInvalid()
        
        if ' ' in username:
            raise UsernameInvalid()

    @property
    def value(self) -> str:
        return self._username

    def __str__(self) -> str:
        return self._username

    def __eq__(self, other) -> bool:
        if isinstance(other, Username):
            return self._username == other._username
        return False
