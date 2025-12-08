
import json
import re
from django.http import HttpRequest, JsonResponse
from django.views import View

from src.application.dtos.user_controller_dto import DeleteUserControllerOutDTO, GetUserControllerOutDTO, SearchUserControllerOutDTO, UpdateUserControllerInDTO, UpdateUserControllerOutDTO
from src.application.errors.auth_errors import NeedAuthentication
from src.application.errors.common_errors import BodyParserError, ParamParserError
from src.application.errors.user_errors import UserNotFound
from src.application.providers import get_decode_token_use_case, get_delete_user_use_case, get_search_user_use_case, get_update_user_use_case, get_user_use_case

class AccountController(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.get_user_use_case = get_user_use_case()
        self.decode_token_use_case = get_decode_token_use_case()
        self.update_user_use_case = get_update_user_use_case()
        self.delete_user_use_case = get_delete_user_use_case()
        self.search_user_use_case = get_search_user_use_case()

    def _get_user_controller(self, request: HttpRequest, *args, **kargs):
        
        authorization_header = request.headers.get("Authorization")
        if authorization_header is None: raise NeedAuthentication
        
        token = authorization_header.split(" ")[1]
        auth_user = self.decode_token_use_case.execute(token)

        user = self.get_user_use_case.execute(auth_user.id)
        if user is None: raise UserNotFound

        return JsonResponse(
            GetUserControllerOutDTO(**user).model_dump()
        )
    
    def _search_user_controller(self, request: HttpRequest, *args, **kargs):
        
        try:
            query = request.GET.get("query")
            length = int(request.GET.get("length")) or 1
            segment = int(request.GET.get("segment")) or 1
        except:
            raise ParamParserError
        
        users_segment = self.search_user_use_case.execute(query, length, segment)
        
        return JsonResponse(
            SearchUserControllerOutDTO(
                users=[
                    GetUserControllerOutDTO(
                        id=user.id,
                        username=user.username.value,
                        email=user.email.value,
                        role=user.role.value,
                    )
                    for user in users_segment.users
                ],
                next_segment=users_segment.next_segment
            ).model_dump()
        )
        

    def get(self, request: HttpRequest, *args, **kargs):
        
        if request.GET.get("query") is None:
            return self._get_user_controller(request, args, kargs)
        else:
            return self._search_user_controller(request, args, kargs)
        

    def put(self, request: HttpRequest):

        authorization_header = request.headers.get("Authorization")

        if authorization_header is None: raise NeedAuthentication
        token = authorization_header.split(" ")[1]

        try:
            raw_data = json.loads(request.body)
            update_user_dto = UpdateUserControllerInDTO(**raw_data)
        except: 
            raise BodyParserError

        auth_user = self.decode_token_use_case.execute(token)

        user = self.update_user_use_case.execute(auth_user.id, update_user_dto.username)

        return JsonResponse(
            UpdateUserControllerOutDTO(
                id=user.id,
                email=user.email,
                username=user.username,
                role=user.role
            ).model_dump()
        )

    def delete(self, request: HttpRequest):

        authorization_header = request.headers.get("Authorization")

        if authorization_header is None: raise NeedAuthentication
        token = authorization_header.split(" ")[1]

        auth_user = self.decode_token_use_case.execute(token)

        self.delete_user_use_case.execute(auth_user.id)

        return JsonResponse(
            DeleteUserControllerOutDTO(
                status="ok"
            ).model_dump()
        )


        
