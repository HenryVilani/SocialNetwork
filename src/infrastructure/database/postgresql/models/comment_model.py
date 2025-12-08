
from datetime import datetime
from sqlalchemy import UUID, Column, String, ForeignKey, DateTime
from .base_model import Base


class CommentModel(Base):

    __tablename__ = "comments"

    id: UUID = Column(UUID, primary_key=True)

    user_id: UUID = Column(UUID, ForeignKey("users.id"), nullable=False)
    post_id: UUID = Column(UUID, ForeignKey("posts.id"), nullable=False)

    content: str = Column(String, nullable=False)

    created_at: datetime = Column(DateTime, default=datetime.now())
