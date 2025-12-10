
from datetime import datetime
from typing import Optional
from sqlalchemy import Column, ForeignKey, String, DateTime
from sqlalchemy.dialects.postgresql import ARRAY
from .base_model import Base


class PostModel(Base):

    __tablename__ = "posts"
    __table_args__ = {'schema': 'public'}

    id: str = Column(String, primary_key=True)
    user_id: str = Column(String, ForeignKey("public.users.id"))

    channel_id: Optional[str] = Column(String, ForeignKey("public.channels.id"), nullable=True)

    title: str = Column(String, nullable=False)
    content: str = Column(String, nullable=False)

    tags: str = Column(ARRAY(String), nullable=False)

    created_at: datetime = Column(DateTime, nullable=False, default=datetime.now())
