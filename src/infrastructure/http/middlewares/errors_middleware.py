
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.utils.deprecation import MiddlewareMixin

from src.application.dtos.comment_repo_dto import ErrorOutDTO
from src.application.errors.base_errors import BaseError
from src.application.errors.common_errors import InternalError

class ErrorHandlingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def process_exception(self, request: HttpRequest, exception: Exception) -> HttpResponse | None:

        print(exception)

        if isinstance(exception, BaseError):
            exception: BaseError
            return JsonResponse(
                ErrorOutDTO(
                    status=exception.message
                ).model_dump(),
                status=400
            )

        else:
            return JsonResponse(
                ErrorOutDTO(
                    status=InternalError().message
                ).model_dump(),
                status=400
            )

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
