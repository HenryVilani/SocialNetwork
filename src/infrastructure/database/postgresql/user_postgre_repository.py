
from uuid import uuid4
from sqlalchemy import exists, select
from sqlalchemy.orm import Session
from src.application.dtos.user_repo_dto import CreateUserRepoInDTO, SegmentUserRepoOutDTO, UpdateUserRepoInDTO
from src.application.errors.user_errors import UserAlreadyExists, UserNotFound
from src.domain.entities.user_entity import User, UserRole
from src.domain.repositories.user_repository import IUserRepository
from src.domain.value_object.email_value_object import Email
from src.domain.value_object.password_value_object import Password
from src.domain.value_object.username_value_object import Username
from src.infrastructure.database.postgresql.database_connection import DatabaseConnection
from src.infrastructure.database.postgresql.models.user_model import UserModel
from src.infrastructure.database.postgresql.breaker_connection import breaker

class UserPostgreRepository(IUserRepository):
    
    def __init__(self, connection: DatabaseConnection):
        self.connection = connection

        self.connection.create_all_tables()

    @breaker
    def create(self, user: CreateUserRepoInDTO) -> User:
        
        with self.connection.session_factory() as session:
            session: Session

            stmt = select(exists().where(UserModel.email == user.email.value))
            if session.execute(stmt).scalar(): raise UserAlreadyExists

            entity = UserModel(
                id=uuid4(),
                username=user.username.value,
                email=user.email.value,
                role=user.role.value,
                password=user.password.value
            )
            session.add(entity)            
            session.commit()

            return User(
                id=str(entity.id),
                username=Username(entity.username),
                email=Email(entity.email),
                password=Password(entity.password, True),
                role=UserRole(entity.role)
            )
    
    @breaker
    def update(self, user_id: str, user: UpdateUserRepoInDTO) -> User:
        
        with self.connection.session_factory() as session:

            session: Session

            entity = session.query(UserModel).filter(UserModel.id == user_id).one_or_none()

            if entity is None: raise UserNotFound

            if user.username:
                entity.username = user.username.value
            
            if user.role:
                entity.role = user.role.value
            
            if user.email:
                entity.email = user.email.value

            if user.password:
                entity.password = user.password.value
            
            session.flush()
            session.commit()

        return User(
            id=str(entity.id),
            username=Username(entity.username),
            email=Email(entity.email),
            password=Password(entity.password, True),
            role=UserRole(entity.role)
        )

    @breaker
    def delete(self, user_id: str) -> None:
        
        with self.connection.session_factory() as session:

            session: Session

            entity = session.query(UserModel).filter(UserModel.id == user_id).one_or_none()
            if entity is None: raise UserNotFound

            session.delete(entity)
            session.commit()

    @breaker
    def find_by_id(self, user_id: str) -> User | None:

        with self.connection.session_factory() as session:

            session: Session

            entity = session.query(UserModel).filter(UserModel.id == user_id).one_or_none()

            if not entity: return None

            return User(
                id=str(entity.id),
                username=Username(entity.username),
                email=Email(entity.email),
                password=Password(entity.password, True),
                role=UserRole(entity.role)
            )

    @breaker
    def find_all_by_username(self, username: str, length: int, segment: int) -> SegmentUserRepoOutDTO:

        with self.connection.session_factory() as session:
            session: Session
            
            offset = (max(segment, 1) - 1) * max(length, 1)

            entities = (
                session.query(UserModel)
                .filter(UserModel.username.ilike(f"%{username}%"))
                .offset(offset)
                .limit(max(length, 1) + 1)
                .all()
            )

            has_next = len(entities) > length
            users = entities[:length]

            return SegmentUserRepoOutDTO(
                users=[
                    User(
                        id=str(entity.id),
                        username=Username(entity.username),
                        email=Email(entity.email),
                        password=Password(entity.password, True),
                        role=UserRole(entity.role)
                    )
                    for entity in users
                ],
                next_segment=(max(segment, 1) + 1) if has_next else None,
            )

    @breaker
    def find_by_email(self, email: Email):
        
        with self.connection.session_factory() as session:

            session: Session

            entity = session.query(UserModel).filter(UserModel.email == email.value).one_or_none()
            if entity is None: raise UserNotFound

            return User(
                id=str(entity.id),
                username=Username(entity.username),
                email=Email(entity.email),
                password=Password(entity.password, True),
                role=UserRole(entity.role)
            )
