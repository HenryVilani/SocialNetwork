
import json
from typing import Optional
from django.http import HttpRequest, JsonResponse
from django.views import View
from src.application.dtos.channel_controller_dto import ChannelDTO, CreateChannelControllerInDTO, CreateChannelControllerOutDTO, DeleteChannelControllerOutDTO, GetChannelControllerOutDTO, SearchChannelControllerOutDTO
from src.application.errors.auth_errors import NeedAuthentication
from src.application.errors.common_errors import BodyParserError, ParamParserError
from src.application.providers import get_create_channel_use_case, get_decode_token_use_case, get_delete_channel_use_case, get_get_channel_use_case, get_search_channel_use_case


class ChannelController(View):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.decode_token_use_case = get_decode_token_use_case()
        
        self.create_channel_use_case = get_create_channel_use_case()
        self.get_channel_use_case = get_get_channel_use_case()
        self.search_channel_use_case = get_search_channel_use_case()
        self.get_channel_use_case = get_get_channel_use_case()
        self.delete_channel_use_case = get_delete_channel_use_case()
    
    def _get_channel_controller(self, request: HttpRequest, channel_id: str):
        
        print(channel_id)
        channel = self.get_channel_use_case.execute(channel_id)
        
        return JsonResponse(
            GetChannelControllerOutDTO(
                id=channel.id,
                name=channel.name,
                description=channel.description,
                posts=channel.posts,
                created_at=channel.created_at
            ).model_dump()
        )
    
    def _list_channels_controller(self, request: HttpRequest):
        
        try:
            query = request.GET.get("query")
            length = int(request.GET.get("length") or "10")
            segment = int(request.GET.get("segment") or "1")
        except:
            raise ParamParserError
        
        segment_channel = self.search_channel_use_case.execute(query, length, segment)
        
        return JsonResponse(
            SearchChannelControllerOutDTO(
                channels=[
                    ChannelDTO(
                        id=channel.id,
                        name=channel.name,
                        description=channel.description,
                        posts=channel.posts,
                        created_at=channel.created_at
                    )
                    for channel in segment_channel.channels
                ],
                next_segment=segment_channel.next_segment
            ).model_dump()
        )
    
    def get(self, request: HttpRequest, *args, **kwargs):
        
        channel_id: Optional[str] = kwargs.get("channel_id")
        
        if channel_id is None:
            return self._list_channels_controller(request)
        else:
            return self._get_channel_controller(request, channel_id)
    
    def post(self, request: HttpRequest):
        
        authorization_header = request.headers.get("Authorization")
        if authorization_header is None: raise NeedAuthentication
        token = authorization_header.split(" ")[1]
        
        try:
            raw_data = json.loads(request.body)
            create_channel_dto = CreateChannelControllerInDTO(**raw_data)
        except: 
            raise BodyParserError
        
        auth_user = self.decode_token_use_case.execute(token)
        
        channel = self.create_channel_use_case.execute(
            auth_user.id,
            create_channel_dto.name,
            create_channel_dto.description
        )
        
        return JsonResponse(
            CreateChannelControllerOutDTO(
                id=channel.id,
                name=channel.name,
                description=channel.description,
                posts=channel.posts,
                created_at=channel.created_at
            ).model_dump()
        )
    
    def delete(self, request: HttpRequest, channel_id: str):
        
        authorization_header = request.headers.get("Authorization")
        if authorization_header is None: raise NeedAuthentication
        token = authorization_header.split(" ")[1]
        
        auth_user = self.decode_token_use_case.execute(token)
        
        self.delete_channel_use_case.execute(auth_user.id, channel_id)
        
        return JsonResponse(
            DeleteChannelControllerOutDTO(
                status="ok"
            ).model_dump()
        )
        
    
