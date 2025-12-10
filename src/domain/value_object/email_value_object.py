import re
from src.application.errors.user_errors import EmailInvalid


class Email:
    """
    Value Object representing an email address.

    This class encapsulates validation rules for email formats and ensures
    that any created instance conforms to standard email constraints.

    :raises EmailInvalid: Raised when the email does not meet format or
        structural requirements.
    """

    def __init__(self, email: str):
        """
        Initialize an Email value object.

        :param email: Raw email address string.
        :type email: str
        """
        self._validate(email)
        self._email = email

    def _validate(self, email: str) -> None:
        """
        Validate the given email address string.

        Validation rules:

        * Length must be between 5 and 254 characters.
        * Must match a valid email format: ``local-part@domain``.
        * Whitespace is not permitted.

        The pattern used enforces a standard RFC-like format:

        ``^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$``

        :param email: Email string to validate.
        :type email: str
        :raises EmailInvalid: If any constraint is violated.
        """
        if not email or len(email) < 5 or len(email) > 254:
            raise EmailInvalid()

        pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
        if not re.match(pattern, email):
            raise EmailInvalid()

        if ' ' in email:
            raise EmailInvalid()

    @property
    def value(self) -> str:
        """
        Return the underlying validated email address.

        :return: Email string.
        :rtype: str
        """
        return self._email

    def __str__(self) -> str:
        """
        Return the email address as a plain string.

        :return: Email as string.
        :rtype: str
        """
        return self._email

    def __eq__(self, other) -> bool:
        """
        Compare two Email value objects for equality.

        :param other: Object to compare against.
        :return: ``True`` if both represent the same email address.
        :rtype: bool
        """
        if isinstance(other, Email):
            return self._email == other._email
        return False
