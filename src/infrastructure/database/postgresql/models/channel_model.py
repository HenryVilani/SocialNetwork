
from datetime import datetime
from sqlalchemy import Column, ForeignKey, String, Integer, DateTime

from src.infrastructure.database.postgresql.models.base_model import Base


class ChannelModel(Base):
    
    __tablename__ = "channels"
    __table_args__ = {'schema': 'public'}

    id: str = Column(String, primary_key=True)
    user_id: str = Column(String, ForeignKey("public.users.id"))
    name: str = Column(String, nullable=False)
    description: str = Column(String, nullable=False)
    posts: int = Column(Integer, nullable=False, default=0)
    created_at: datetime = Column(DateTime, nullable=False, default=datetime.now())

