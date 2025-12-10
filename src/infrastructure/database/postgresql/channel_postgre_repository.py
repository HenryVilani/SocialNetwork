
from uuid import uuid4
from sqlalchemy.orm import Session
from src.application.dtos.channel_repo_dto import CreateChannelRepoInDTO, SegmentChannelRepoOutDTO, UpdateChannelRepoInDTO
from src.application.errors.channel_erros import ChannelNotFoundError
from src.domain.entities.channel_entity import Channel
from src.domain.repositories.channel_repository import IChannelRepository
from src.infrastructure.database.postgresql.database_connection import DatabaseConnection
from src.infrastructure.database.postgresql.breaker_connection import breaker
from src.infrastructure.database.postgresql.models.channel_model import ChannelModel

class ChannelPostgreRepository(IChannelRepository):

    def __init__(self, connection: DatabaseConnection):
        self.connection = connection
        

    @breaker
    def create(self, channel: CreateChannelRepoInDTO):
        
        with self.connection.session_factory() as session:
            session: Session

            entity = ChannelModel(
                id=uuid4().hex,
                user_id=channel.user_id,
                name=channel.name,
                description=channel.description
            )

            session.add(entity)
            session.commit()

            return Channel(
                id=str(entity.id),
                user_id=str(entity.user_id),
                name=entity.name,
                description=entity.description,
                posts=entity.posts,
                created_at=entity.created_at
            )
    
    @breaker
    def update(self, channel_id: str, channel: UpdateChannelRepoInDTO) -> Channel:
        
        with self.connection.session_factory() as session:
            session: Session

            entity = ChannelModel(
                name=channel.name,
                description=channel.description
            )

            entity = session.query(ChannelModel).filter(ChannelModel.id == channel_id).one_or_none()
            if entity is None: raise ChannelNotFoundError

            if channel.description:
                entity.description = channel.description

            if channel.name:
                entity.name = channel.name

            session.commit()

            return Channel(
                id=str(entity.id),
                user_id=str(entity.user_id),
                name=entity.name,
                description=entity.description,
                posts=entity.posts,
                created_at=entity.created_at
            )
        
    @breaker
    def delete(self, channel_id: str) -> None:

        with self.connection.session_factory() as session:
            session: Session

            entity = session.query(ChannelModel).filter(ChannelModel.id == channel_id).one_or_none()
            if entity is None: raise ChannelNotFoundError

            session.delete(entity)
            session.commit()
            
    @breaker
    def delete_all_by_user(self, user_id):
        
        with self.connection.session_factory() as session:
            session: Session

            entities = session.query(ChannelModel).filter(ChannelModel.user_id == user_id).all()

            for entity in entities:
                session.delete(entity)
                
            session.commit()

    @breaker
    def find_by_id(self, channel_id: str) -> Channel | None:
        
        with self.connection.session_factory() as session:
            session: Session

            entity = session.query(ChannelModel).filter(ChannelModel.id == channel_id).one_or_none()
            if entity is None: return None

            return Channel(
                id=str(entity.id),
                user_id=str(entity.user_id),
                name=entity.name,
                description=entity.description,
                posts=entity.posts,
                created_at=entity.created_at
            ) 

    @breaker
    def find_all_by_name(self, name: str, length: int, segment: int) -> SegmentChannelRepoOutDTO:
        
        with self.connection.session_factory() as session:
            session: Session
            
            offset = (max(segment, 1) - 1) * max(length, 1)

            entities = (
                session.query(ChannelModel)
                .filter(ChannelModel.name.ilike(f"%{name}%"))
                .offset(offset)
                .limit(max(length, 1) + 1)
                .all()
            )
            
            has_next = len(entities) > length
            channels = entities[:length]
            
            return SegmentChannelRepoOutDTO(
                channels=[
                    Channel(
                        id=str(entity.id),
                        user_id=str(entity.user_id),
                        name=entity.name,
                        description=entity.description,
                        posts=entity.posts,
                        created_at=entity.created_at
                    )
                    for entity in entities    
                ],
                next_segment=(max(segment, 1) + 1) if has_next else None,
            )

            

            
