import re
from src.application.errors.user_errors import EmailInvalid


class Email:

    def __init__(self, email: str):
        self._validate(email)
        self._email = email

    def _validate(self, email: str) -> None:
        if not email or len(email) < 5 or len(email) > 254:
            raise EmailInvalid()

        pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
        if not re.match(pattern, email):
            raise EmailInvalid()

        if ' ' in email:
            raise EmailInvalid()

    @property
    def value(self) -> str:
        return self._email

    def __str__(self) -> str:
        return self._email

    def __eq__(self, other) -> bool:
        if isinstance(other, Email):
            return self._email == other._email
        return False