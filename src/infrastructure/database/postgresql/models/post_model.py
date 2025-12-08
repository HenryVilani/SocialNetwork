
from datetime import datetime
from typing import Optional
from uuid import uuid4
from sqlalchemy import UUID, Column, ForeignKey, String, DateTime
from sqlalchemy.dialects.postgresql import ARRAY
from .base_model import Base


class PostModel(Base):

    __tablename__ = "posts"

    id: UUID = Column(UUID, primary_key=True)
    user_id: UUID = Column(UUID, ForeignKey("users.id"))

    channel_id: Optional[UUID] = Column(UUID, ForeignKey("channels.id"), nullable=True)

    title: str = Column(String, nullable=False)
    content: str = Column(String, nullable=False)

    tags: str = Column(ARRAY(String), nullable=False)

    created_at: datetime = Column(DateTime, nullable=False, default=datetime.now())
