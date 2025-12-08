import re
from src.application.errors.user_errors import PasswordInvalid
from argon2 import PasswordHasher

class Password:

    def __init__(self, password: str, hashed=False):
        if hashed:
            self._password = password
        else:
            self._validate(password)
            self._password = self._hash(password)


    def _validate(self, password: str) -> None:
        if not password or len(password) < 8 or len(password) > 25:
            raise PasswordInvalid()

        if ' ' in password or '\t' in password or '\n' in password:
            raise PasswordInvalid()

        if not re.match(r'^[\x20-\x7E]+$', password):
            raise PasswordInvalid()

    def _hash(self, password: str) -> str:
        hasher = PasswordHasher()
        return hasher.hash(password)

    @property
    def value(self) -> str:
        return self._password

    @staticmethod
    def verify(password: Password, raw_password: str) -> bool:
        hasher = PasswordHasher()
        try:
            hasher.verify(password.value, raw_password)
            return True
        except:
            return False


    def __str__(self) -> str:
        return self._password

    def __eq__(self, other) -> bool:
        if isinstance(other, Password):
            return self._password == other._password
        return False
