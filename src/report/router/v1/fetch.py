from fastapi import Request
from utilsfastapi.utilsfastapi.response.custom_orjson_response import ProjectJSONResponse as JsonResponse

from ... import NAME
from ...service.v1 import fetch as service
from .router import router

ROUTE_NAME = 'get_' + NAME


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
