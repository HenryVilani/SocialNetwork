
import os
from sqlalchemy import Engine, create_engine, text
from sqlalchemy.orm import sessionmaker
from tenacity import retry, stop_after_attempt, wait_exponential

from src.infrastructure.database.postgresql.models.base_model import Base

class DatabaseConnection:

    _engine: Engine
    _session_factory: sessionmaker

    def __init__(self):
        self._engine = create_engine(
            os.getenv("DATABASE_URL"),
            pool_pre_ping=True,
            echo=False
        ).execution_options(autocommit=False)
        self._session_factory = sessionmaker(
            bind=self._engine,
            autoflush=False
        )

    def create_all_tables(self):
        Base.metadata.create_all(bind=self._engine)

    @retry(
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=1, min=1, max=10)
    )   
    def _try_connection(self):
        
        with self._session_factory() as session:

            session.execute(text("SELECT 1"))

    def try_connection(self) -> bool:

        try:
            self._try_connection()
            return True
        except:
            return False     
    
    @property
    def engine(self):
        return self._engine
    
    @property
    def session_factory(self):
        return self._session_factory

connection = DatabaseConnection()
