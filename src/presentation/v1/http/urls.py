from django.urls import path

from src.presentation.v1.http import auth_controller, channel_controller, comment_controller, post_controller
from src.presentation.v1.http import account_controller

urlpatterns = [
    path('v1/login', auth_controller.login_user),
    path('v1/register', auth_controller.register_user),

    path('v1/account', account_controller.AccountController.as_view()),
    
    path('v1/posts', post_controller.PostController.as_view()),
    path('v1/posts/<str:post_id>', post_controller.PostController.as_view()),
    
    path('v1/channels', channel_controller.ChannelController.as_view()),
    path('v1/channels/<str:channel_id>', channel_controller.ChannelController.as_view()),
    
    path('v1/comments/<str:id>', comment_controller.CommentController.as_view()),
]
