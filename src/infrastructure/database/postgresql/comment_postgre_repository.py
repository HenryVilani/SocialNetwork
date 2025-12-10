
from typing import List, Optional
from uuid import uuid4
from sqlalchemy.orm import Session
from src.application.dtos.comment_repo_dto import CreateCommentRepoInDTO
from src.application.errors.comment_errors import CommentNotFoundError
from src.domain.entities.comment_entity import Comment
from src.domain.repositories.comment_repository import ICommentRepository
from src.infrastructure.database.postgresql.database_connection import DatabaseConnection
from src.infrastructure.database.postgresql.models.comment_model import CommentModel
from src.infrastructure.database.postgresql.breaker_connection import breaker

class CommentPostgreRepository(ICommentRepository):

    def __init__(self, connection: DatabaseConnection):
        self.connection = connection
        

    @breaker
    def create(self, comment: CreateCommentRepoInDTO):
        
        with self.connection.session_factory() as session:
            session: Session

            entity = CommentModel(
                id=uuid4().hex,
                user_id=comment.user_id,
                post_id=comment.post_id,
                content=comment.content
            )

            session.add(entity)
            session.commit()

            return Comment(
                id=str(entity.id),
                user_id=str(entity.user_id),
                post_id=str(entity.post_id),
                content=entity.content,
                created_at=entity.created_at
            )

    @breaker
    def delete(self, comment_id: str):
        
        with self.connection.session_factory() as session:
            session: Session

            entity = session.query(CommentModel).filter(CommentModel.id == comment_id).one_or_none()
            if entity is None: CommentNotFoundError

            session.delete(entity)
            session.commit()
            
    @breaker
    def delete_all_by_user(self, user_id: str):
        with self.connection.session_factory() as session:
            session: Session

            entities = session.query(CommentModel).filter(CommentModel.user_id == user_id).all()
        
            for entity in entities:
                session.delete(entity)
                
            session.commit()

    @breaker
    def find_all_by_post(self, post_id: str, length: int, segment: int) -> List[Comment]:
        
        with self.connection.session_factory() as session:
            session: Session

            entities = (
                session.query(CommentModel)
                .filter(CommentModel.post_id == post_id)
                .offset(segment)
                .limit(length)
                .all()
            )

            return [
                Comment(
                    id=str(entity.id),
                    user_id=str(entity.user_id),
                    post_id=str(entity.post_id),
                    content=entity.content,
                    created_at=entity.created_at
                )
                for entity in entities
            ]

    @breaker
    def find_all_by_user(self, user_id: str, length: int, segment: int):
        
        with self.connection.session_factory() as session:
            session: Session
        
            entities = (
                session.query(CommentModel)
                .filter(CommentModel.user_id == user_id)
                .offset(segment)
                .limit(length)
                .all()
            )

            return [
                Comment(
                    id=str(entity.id),
                    user_id=str(entity.user_id),
                    post_id=str(entity.post_id),
                    content=entity.content,
                    created_at=entity.created_at
                )
                for entity in entities
            ]

    @breaker
    def find_by_id(self, comment_id: str) -> Optional[Comment]:
        
        with self.connection.session_factory() as session:
            session: Session
            
            entity = session.query(CommentModel).filter(CommentModel.id == comment_id).one_or_none()
            if entity is None: return None
            
            return Comment(
                id=str(entity.id),
                user_id=str(entity.user_id),
                post_id=str(entity.post_id),
                content=entity.content,
                created_at=entity.created_at
            )
        
