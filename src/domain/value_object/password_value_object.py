import re
from src.application.errors.user_errors import PasswordInvalid
from argon2 import PasswordHasher


class Password:
    """
    Value Object representing a password.

    This class provides validation and hashing for user passwords.
    Raw passwords are validated and hashed using *argon2*, while
    pre-hashed passwords can be passed directly when ``hashed=True``.

    :raises PasswordInvalid: Raised when the provided password does not meet
        format, size, or character requirements.
    """

    def __init__(self, password: str, hashed: bool = False):
        """
        Initialize a Password value object.

        :param password: Raw or hashed password string.
        :type password: str
        :param hashed: Indicates whether the provided string is already hashed.
        :type hashed: bool
        """
        if hashed:
            self._password = password
        else:
            self._validate(password)
            self._password = self._hash(password)

    def _validate(self, password: str) -> None:
        """
        Validate the given raw password string.

        Validation rules:

        * Length must be between 8 and 25 characters.
        * Whitespace characters (space, tab, newline) are not permitted.
        * Only printable ASCII characters (0x20–0x7E) are allowed.

        :param password: Password string to validate.
        :type password: str
        :raises PasswordInvalid: If the password violates any rule.
        """
        if not password or len(password) < 8 or len(password) > 25:
            raise PasswordInvalid()

        if ' ' in password or '\t' in password or '\n' in password:
            raise PasswordInvalid()

        if not re.match(r'^[\x20-\x7E]+$', password):
            raise PasswordInvalid()

    def _hash(self, password: str) -> str:
        """
        Hash the given raw password using *argon2*.

        :param password: Plain text password.
        :type password: str
        :return: The hashed password.
        :rtype: str
        """
        hasher = PasswordHasher()
        return hasher.hash(password)

    @property
    def value(self) -> str:
        """
        Return the underlying hashed password string.

        :return: Hashed password.
        :rtype: str
        """
        return self._password

    @staticmethod
    def verify(password: "Password", raw_password: str) -> bool:
        """
        Verify a raw password against a stored hashed password.

        :param password: Password value object containing the hashed password.
        :type password: Password
        :param raw_password: Raw password to verify.
        :type raw_password: str
        :return: ``True`` if the raw password matches the hash, otherwise ``False``.
        :rtype: bool
        """
        hasher = PasswordHasher()
        try:
            hasher.verify(password.value, raw_password)
            return True
        except Exception:
            return False

    def __str__(self) -> str:
        """
        Return the hashed password as a plain string.

        :return: Hashed password.
        :rtype: str
        """
        return self._password

    def __eq__(self, other) -> bool:
        """
        Compare this Password instance with another.

        :param other: Object to compare against.
        :return: ``True`` if both objects contain the same hashed password.
        :rtype: bool
        """
        if isinstance(other, Password):
            return self._password == other._password
        return False
