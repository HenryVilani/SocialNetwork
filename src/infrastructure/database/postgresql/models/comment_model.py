
from datetime import datetime
from sqlalchemy import Column, String, ForeignKey, DateTime
from .base_model import Base


class CommentModel(Base):

    __tablename__ = "comments"
    __table_args__ = {'schema': 'public'}

    id: str = Column(String, primary_key=True)

    user_id: str = Column(String, ForeignKey("public.users.id"), nullable=False)
    post_id: str = Column(String, ForeignKey("public.posts.id"), nullable=False)

    content: str = Column(String, nullable=False)

    created_at: datetime = Column(DateTime, default=datetime.now())
