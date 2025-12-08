
from pybreaker import CircuitBreaker, CircuitBreakerListener

from src.application.errors.base_errors import BaseError
from src.application.errors.common_errors import InternalError
from src.infrastructure.database.postgresql.database_connection import DatabaseConnection, connection


class BreakerListener(CircuitBreakerListener):

    def __init__(self, connection: DatabaseConnection):
        self.connection = connection

    def failure(self, cb, exc):

        if isinstance(exc, BaseError):
            raise exc
        else:
            self.connection.try_connection()
            raise InternalError from exc



breaker = CircuitBreaker(
    fail_max=3,
    reset_timeout=10,
    listeners=[BreakerListener(connection)]
)
