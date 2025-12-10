
from datetime import datetime
import uuid
from sqlalchemy import Column, String, Enum, DateTime
from src.domain.entities.user_entity import UserRole
from .base_model import Base


class UserModel(Base):

    __tablename__ = "users"
    __table_args__ = {'schema': 'public'}

    id: str = Column(String, primary_key=True, default=uuid.uuid4().hex)
    username: str = Column(String, nullable=False, unique=True)
    email: str = Column(String, nullable=False, unique=True)
    role: UserRole = Column(Enum(UserRole), nullable=False)
    password: str = Column(String, nullable=False)

    created_at: datetime = Column(DateTime, nullable=False, default=datetime.now())
