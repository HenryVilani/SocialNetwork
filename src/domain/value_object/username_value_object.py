
import re
from src.application.errors.user_errors import UsernameInvalid


class Username:
    """
    Value Object representing a username.

    This class encapsulates username validation rules and guarantees
    that any instance created adheres to the defined constraints.

    :raises UsernameInvalid: Raised when the provided username does not meet 
        format, size, or character requirements.
    """

    def __init__(self, username: str):
        """
        Initialize a Username value object.

        :param username: Raw username string.
        """
        self._validate(username)
        self._username = username

    def _validate(self, username: str) -> None:
        """
        Validate the given username string.

        Validation rules:
        
        * Length must be between 5 and 25 characters.
        * Allowed characters: letters, digits, dot, hyphen.
        * Whitespace is not permitted.

        :param username: Username string to validate.
        :type username: str
        :raises UsernameInvalid: If the username violates any constraint.
        """
        
        if not username or len(username) < 5 or len(username) > 25:
            raise UsernameInvalid()
        
        if not re.match(r'^[a-zA-Z0-9.\-]+$', username):
            raise UsernameInvalid()
        
        if ' ' in username:
            raise UsernameInvalid()

    @property
    def value(self) -> str:
        """
        Return the underlying username string.

        :return: The validated username value.
        """
        return self._username

    def __str__(self) -> str:
        """
        Return the username as a plain string.

        :return: Username as string.
        """
        return self._username

    def __eq__(self, other) -> bool:
        """
        Compare this Username instance with another.

        :param other: Object to compare against.
        :return: ``True`` if both objects represent the same username, 
            ``False`` otherwise.
        """
        if isinstance(other, Username):
            return self._username == other._username
        return False
    

    