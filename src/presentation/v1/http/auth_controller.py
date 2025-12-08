
import json
from django.http import HttpRequest, JsonResponse

from src.application.dtos.user_controller_dto import CreateUseControllerOutDTO, CreateUserControllerInDTO, LoginUserControllerInDTO, LoginUserControllerOutDTO
from src.application.errors.common_errors import BodyParserError, MethodError
from src.application.providers import get_create_user_use_case, get_login_user_use_case
from src.domain.entities.user_entity import User, UserRole

def login_user(request: HttpRequest):

    if request.method != "POST":
        raise MethodError
    
    try:
        raw_data = json.loads(request.body)
        login_user_dto = LoginUserControllerInDTO(**raw_data)
    except:
        raise BodyParserError
    
    login_user_use_case = get_login_user_use_case()

    
    token = login_user_use_case.execute(login_user_dto.email, login_user_dto.password)

    return JsonResponse(
        LoginUserControllerOutDTO(
            token=token
        ).model_dump()
    )


def register_user(request: HttpRequest):

    if request.method != 'POST':
        raise MethodError
    
    try:
        raw_data = json.loads(request.body)
        create_user_dto = CreateUserControllerInDTO(**raw_data)
    except:
        raise BodyParserError

    create_user_use_case = get_create_user_use_case()

    user: User = create_user_use_case.execute(
        username=create_user_dto.username,
        email=create_user_dto.email,
        role=UserRole.USER,
        password=create_user_dto.password
    )


    return JsonResponse(CreateUseControllerOutDTO(
        id=user.id,
        username=user.username.value,
        email=user.email.value,
        role=user.role.value
    ).model_dump())
