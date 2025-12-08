
import json
from django.http import HttpRequest, JsonResponse
from django.views import View

from src.application.dtos.comment_controller_dto import CreateCommentControllerInDTO, CreateCommentControllerOutDTO, DeleteCommentControllerOutDTO, ListCommentByPostControllerOutDTO
from src.application.errors.auth_errors import NeedAuthentication
from src.application.errors.common_errors import BodyParserError, ParamParserError
from src.application.providers import get_create_comment_use_case, get_decode_token_use_case, get_delete_comment_use_case, get_list_comment_by_post_use_case


class CommentController(View):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.decode_token_use_case = get_decode_token_use_case()
        self.create_comment_use_case = get_create_comment_use_case()
        self.list_by_post_use_case = get_list_comment_by_post_use_case()
        self.delete_comment_use_case = get_delete_comment_use_case()
            
    def get(self, request: HttpRequest, post_id: str):
        
        try:
            length = int(request.GET.get("length") or "10")
            segment = int(request.GET.get("segment") or "1")
        except:
            raise ParamParserError
        
        comment_segment = self.list_by_post_use_case.execute(post_id, length, segment)
        
        return JsonResponse(
            ListCommentByPostControllerOutDTO(
                comments=comment_segment.comments,
                next_segment=comment_segment.next_segment
            ).model_dump()
        )
    
    def post(self, request: HttpRequest, post_id: str):
        
        authorization_header = request.headers.get("Authorization")
        if authorization_header is None: raise NeedAuthentication
        token = authorization_header.split(" ")[1]
        
        try:
            raw_data = json.loads(request.body)
            create_comment_dto = CreateCommentControllerInDTO(**raw_data)
        except: 
            raise BodyParserError

        auth_user = self.decode_token_use_case.execute(token)
        
        comment = self.create_comment_use_case.execute(auth_user.id, post_id, create_comment_dto.content)
        
        return JsonResponse(
            CreateCommentControllerOutDTO(
                id=comment.id,
                content=comment.content
            ).model_dump()
        )
    
    def delete(self, request: HttpRequest, comment_id: str):
        
        authorization_header = request.headers.get("Authorization")
        if authorization_header is None: raise NeedAuthentication
        token = authorization_header.split(" ")[1]
        
        auth_user = self.decode_token_use_case.execute(token)
        
        self.delete_comment_use_case.execute(auth_user.id, comment_id)
        
        return JsonResponse(
            DeleteCommentControllerOutDTO(
                status="ok"
            ).model_dump()
        )
        