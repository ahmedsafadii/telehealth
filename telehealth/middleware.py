from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR
from django.utils.translation import gettext_lazy as _
from rest_framework.views import exception_handler
from telehealth.keys import DEBUG


def json_response(status: bool = True, errors=None, message: str = "", data=None, status_code: int = HTTP_200_OK):

    data = {
        "status": status if errors is None else False,
        "message": message,
        "data": data,
        "errors": errors
    }

    return JsonResponse(data=data, status=status_code)


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    return json_response(status=False, message=exc.detail, status_code=response.status_code)


class CustomMiddleware(MiddlewareMixin):

    def process_exception(self, request, exception):
        # if DEBUG:
        #     raise exception
        return json_response(status=False, message=_("an unexpected error happened which might be temporary"),
                             status_code=HTTP_500_INTERNAL_SERVER_ERROR)
