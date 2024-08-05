from os import sep

from fastapi import Request
from utilsweb.fastapi.response.custom_orjson_response import ProjectJSONResponse as JsonResponse

from ... import LOWER_SNAKE_CASE_NAME
from ...service.v1 import fetch as service
from .router import router

FILE_NAME = __file__.rstrip(".py").rsplit(sep, 1)[-1]
ROUTE_NAME = f"{LOWER_SNAKE_CASE_NAME}:{FILE_NAME}"


@router.get(
    path="/",
    name='get',
    summary='summary',
    description='description',
    response_description='response_description',
    openapi_extra=None,
)
async def fetch(request: Request) -> JsonResponse:
    data = await service(request=request)
    return JsonResponse(**data)
