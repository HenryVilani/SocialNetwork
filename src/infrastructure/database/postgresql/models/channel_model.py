
from datetime import datetime
from sqlalchemy import UUID, Column, ForeignKey, String, Integer, DateTime

from src.infrastructure.database.postgresql.models.base_model import Base


class ChannelModel(Base):
    
    __tablename__ = "channels"

    id: UUID = Column(UUID, primary_key=True)
    user_id: UUID = Column(UUID, ForeignKey("users.id"))
    name: str = Column(String, nullable=False)
    description: str = Column(String, nullable=False)
    posts: int = Column(Integer, nullable=False, default=0)
    created_at: datetime = Column(DateTime, nullable=False, default=datetime.now())

