
from uuid import uuid4
from sqlalchemy.orm import Session
from src.application.dtos.post_repo_dto import CreatePostRepoInDTO, SegmentPostRepoOutDTO
from src.application.errors.post_errors import PostNotFoundError
from src.domain.entities.post_entity import Post
from src.domain.repositories.post_repository import IPostRepository
from src.infrastructure.database.postgresql.breaker_connection import breaker
from src.infrastructure.database.postgresql.database_connection import DatabaseConnection
from src.infrastructure.database.postgresql.models.post_model import PostModel

class PostPostgreRepository(IPostRepository):

    def __init__(self, connection: DatabaseConnection):
        self.connection = connection
        self.connection.create_all_tables()

    @breaker
    def create(self, entity: CreatePostRepoInDTO) -> Post:

        with self.connection.session_factory() as session:
            session: Session

            entity = PostModel(
                id=uuid4(),
                user_id=str(entity.user_id),
                channel_id=entity.channel_id,
                title=entity.title,
                content=entity.content,
                tags=entity.tags
            )

            session.add(entity)
            session.commit()

            return Post(
                id=str(entity.id),
                title=entity.title,
                content=entity.content,
                user_id=str(entity.user_id),
                channel_id=entity.channel_id,
                tags=entity.tags,
                created_at=entity.created_at
            )

    @breaker
    def delete(self, id: str) -> None:

        with self.connection.session_factory() as session:
            session: Session

            post = session.query(PostModel).filter(PostModel.id == id).one_or_none()
            if post is None: raise PostNotFoundError

            session.delete(post)
            session.commit()

    @breaker
    def delete_all_by_user(self, user_id):
        
        with self.connection.session_factory() as session:
            session: Session

            entities = session.query(PostModel).filter(PostModel.user_id == user_id).all()

            for entity in entities:
                session.delete(entity)
            session.commit()
        

    @breaker
    def find_by_id(self, id: str) -> Post | None:

        with self.connection.session_factory() as session:
            session: Session

            entity = session.query(PostModel).filter(PostModel.id == id).one_or_none()
            if entity is None: return None

            return Post(
                id=str(entity.id),
                title=entity.title,
                content=entity.content,
                user_id=str(entity.user_id),
                channel_id=entity.channel_id,
                tags=entity.tags,
                created_at=entity.created_at
            )

    @breaker
    def find_all_by_title(self, title: str, length: int, segment: int) -> SegmentPostRepoOutDTO:

        with self.connection.session_factory() as session:
            session: Session
            

            offset = (max(segment, 1) - 1) * max(length, 1)

            entities = (
                session.query(PostModel)
                .filter(PostModel.title.ilike(f"%{title}%"))
                .offset(offset)
                .limit(max(length, 1) + 1)
                .all()
            )

            has_next = len(entities) > length
            posts = entities[:length]

            return SegmentPostRepoOutDTO(
                posts=[
                   Post(
                        id=str(entity.id),
                        title=entity.title,
                        content=entity.content,
                        user_id=str(entity.user_id),
                        channel_id=entity.channel_id,
                        tags=entity.tags,
                        created_at=entity.created_at
                    )
                    for entity in posts
                ],
                next_segment=(max(segment, 1) + 1) if has_next else None,
            )

    @breaker
    def find_all_by_user(self, user_id: str, length: int, segment: int) -> SegmentPostRepoOutDTO:
        with self.connection.session_factory() as session:
            session: Session
            
            offset = (max(segment, 1) - 1) * max(length, 1)

            entities = (
                session.query(PostModel)
                .filter(PostModel.user_id == user_id)
                .offset(offset)
                .limit(max(length, 1) + 1)
                .all()
            )

            has_next = len(entities) > length
            posts = entities[:length]

            return SegmentPostRepoOutDTO(
                posts=[
                    Post(
                        id=str(entity.id),
                        title=entity.title,
                        content=entity.content,
                        user_id=str(entity.user_id),
                        channel_id=entity.channel_id,
                        tags=entity.tags,
                        created_at=entity.created_at
                    )
                    for entity in posts
                ],
                next_segment=(max(segment, 1) + 1) if has_next else None,
            )


