
from src.application.use_cases.channel.create_use_case import CreateChannelUseCase
from src.application.use_cases.channel.delete_use_case import DeleteChannelUseCase
from src.application.use_cases.channel.get_use_case import GetChannelUseCase
from src.application.use_cases.channel.search_use_case import SearchChannelUseCase
from src.application.use_cases.comment.create_use_case import CreateCommentUseCase
from src.application.use_cases.comment.delete_use_case import DeleteCommentUseCase
from src.application.use_cases.comment.list_by_post_use_case import ListCommentByPostUseCase
from src.application.use_cases.post.create_use_case import CreatePostUseCase
from src.application.use_cases.account.create_use_case import CreateUserUseCase
from src.application.use_cases.auth.decode_token_use_case import DecodeTokenUseCase
from src.application.use_cases.post.delete_use_case import DeletePostUseCase
from src.application.use_cases.account.delete_use_case import DeleteUserUseCase
from src.application.use_cases.post.get_use_case import GetPostUseCase
from src.application.use_cases.account.get_use_case import GetUserUseCase
from src.application.use_cases.auth.login_use_case import LoginUserUseCase
from src.application.use_cases.post.search_post_use_case import SearchPostUseCase
from src.application.use_cases.account.search_use_case import SearchUserUseCase
from src.application.use_cases.account.update_use_case import UpdateUserUseCase

from src.infrastructure.auth.jwt.auth_jwt_repository import AuthJWTRepository
from src.infrastructure.database.postgresql.channel_postgre_repository import ChannelPostgreRepository
from src.infrastructure.database.postgresql.comment_postgre_repository import CommentPostgreRepository
from src.infrastructure.database.postgresql.post_prostgre_repository import PostPostgreRepository
from src.infrastructure.database.postgresql.user_postgre_repository import UserPostgreRepository
from src.infrastructure.database.postgresql.database_connection import connection

def get_user_repository():

    return UserPostgreRepository(connection)

def get_auth_repository():

    return AuthJWTRepository()

def get_post_repository():
    
    return PostPostgreRepository(connection)

def get_comment_repository():
    
    return CommentPostgreRepository(connection)

def get_channel_repository():
    
    return ChannelPostgreRepository(connection)


def get_login_user_use_case():

    user_repository = get_user_repository()
    auth_repository = get_auth_repository()

    return LoginUserUseCase(auth_repository, user_repository)

def get_create_user_use_case():

    user_repository = get_user_repository()
    return CreateUserUseCase(user_repository)

def get_user_use_case():

    user_repository = get_user_repository()
    return GetUserUseCase(user_repository)

def get_decode_token_use_case():

    auth_repository = get_auth_repository()
    return DecodeTokenUseCase(auth_repository)

def get_update_user_use_case():

    user_repository = get_user_repository()
    return UpdateUserUseCase(user_repository)

def get_delete_user_use_case():
    
    user_repository = get_user_repository()
    post_repository = get_post_repository()
    comment_repository = get_comment_repository()
    channel_repository = get_channel_repository()
    return DeleteUserUseCase(user_repository, post_repository, comment_repository, channel_repository)

def get_search_user_use_case():
    
    user_repository = get_user_repository()
    return SearchUserUseCase(user_repository)

def get_create_post_use_case():
    
    post_repository = get_post_repository()
    return CreatePostUseCase(post_repository)

def get_post_use_case():
    
    post_repository = get_post_repository()
    return GetPostUseCase(post_repository)

def get_delete_post_use_case():
    
    post_repository = get_post_repository()
    return DeletePostUseCase(post_repository)
    
def get_search_post_use_case():
    
    post_repository = get_post_repository()
    return SearchPostUseCase(post_repository)


def get_create_channel_use_case():
    
    channel_repository = get_channel_repository()
    post_repository = get_post_repository()
    return CreateChannelUseCase(
        post_repository=post_repository,
        channel_repository=channel_repository
    )

def get_search_channel_use_case():
    
    channel_repository = get_channel_repository()
    post_repository = get_post_repository()
    return SearchChannelUseCase(
        post_repository=post_repository,
        channel_repository=channel_repository
    )

def get_delete_channel_use_case():
    
    channel_repository = get_channel_repository()
    return DeleteChannelUseCase(channel_repository)

def get_get_channel_use_case():
    
    channel_repository = get_channel_repository()
    return GetChannelUseCase(channel_repository)


def get_create_comment_use_case():
    
    user_repository = get_user_repository()
    post_repository = get_post_repository()
    comment_repository = get_comment_repository()
    return CreateCommentUseCase(
        user_repository=user_repository,
        post_repository=post_repository,
        comment_repository=comment_repository
    )
    
def get_delete_comment_use_case():
    
    user_repository = get_user_repository()
    comment_repository = get_comment_repository()
    return DeleteCommentUseCase(
        user_repository=user_repository,
        comment_repository=comment_repository
    )
    
def get_list_comment_by_post_use_case():

    post_repository = get_post_repository()
    comment_repository = get_comment_repository()
    return ListCommentByPostUseCase(
        post_repository=post_repository,
        comment_repository=comment_repository
    )