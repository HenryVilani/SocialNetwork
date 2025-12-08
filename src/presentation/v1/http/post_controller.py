
import json
from django.http import HttpRequest, JsonResponse
from django.views import View

from src.application.dtos.post_controller_dto import CreatePostControllerInDTO, CreatePostControllerOutDTO, DeletePostControllerOutDTO, GetPostControllerOutDTO, SearchPostControllerOutDTO
from src.application.errors.auth_errors import NeedAuthentication
from src.application.errors.common_errors import BodyParserError, ParamParserError
from src.application.providers import get_create_post_use_case, get_decode_token_use_case, get_delete_post_use_case, get_post_use_case, get_search_post_use_case


class PostController(View):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.decode_token_use_case = get_decode_token_use_case()
        self.create_post_use_case = get_create_post_use_case()
        self.get_post_use_case = get_post_use_case()
        self.delete_post_use_case = get_delete_post_use_case()
        self.search_post_use_case = get_search_post_use_case()
    
    
    def _get_post_controller(self, request: HttpRequest, post_id: str):
                
        post = self.get_post_use_case.execute(post_id)
        
        return JsonResponse(
            GetPostControllerOutDTO(
                id=post.id,
                title=post.title,
                content=post.content,
                tags=post.tags,
                created_at=post.created_at
            ).model_dump()
        )

    
    def _list_posts_controller(self, request: HttpRequest):
        
        try:
            query = request.GET.get("query")
            length = int(request.GET.get("length")) or 1
            segment = int(request.GET.get("segment")) or 1
        except:
            raise ParamParserError
        
        segment_posts = self.search_post_use_case.execute(query, length, segment)
        
        return JsonResponse(
            SearchPostControllerOutDTO(
                posts=[
                    GetPostControllerOutDTO(
                        id=post.id,
                        title=post.title,
                        content=post.content,
                        tags=post.tags,
                        created_at=post.created_at
                    )
                    for post in segment_posts.posts
                ],
                next_segment=segment_posts.next_segment
            ).model_dump()
        )
        
    
    def get(self, request: HttpRequest, *args, **kwargs):
        
        post_id: str | None = kwargs.get("post_id")
    
        if post_id is None:
            return self._list_posts_controller(request)
        else:
            return self._get_post_controller(request, post_id)
    
    def post(self, request: HttpRequest):

        authorization_header = request.headers.get("Authorization")
        if authorization_header is None: raise NeedAuthentication
        token = authorization_header.split(" ")[1]
        
        try:
            raw_data = json.loads(request.body)
            create_post_dto = CreatePostControllerInDTO(**raw_data)
        except: 
            raise BodyParserError

        auth_user = self.decode_token_use_case.execute(token)
        
        post = self.create_post_use_case.execute(
            auth_user.id,
            create_post_dto.title,
            create_post_dto.content,
            create_post_dto.tags,
            create_post_dto.channel_id
        )
        
        return JsonResponse(
            CreatePostControllerOutDTO(
                id=post.id,
                title=post.title,
                content=post.content,
                tags=post.tags,
                created_at=post.created_at,
                channel_id=post.channel_id
            ).model_dump()
        )

    def delete(self, request: HttpRequest, post_id: str):

        authorization_header = request.headers.get("Authorization")
        if authorization_header is None: raise NeedAuthentication
        token = authorization_header.split(" ")[1]

        auth_user = self.decode_token_use_case.execute(token)
        
        
        self.delete_post_use_case.execute(auth_user.id, post_id)
        
        return JsonResponse(
            DeletePostControllerOutDTO(
                status="ok"
            ).model_dump()
        )
     