from fastapi import Depends
from utilsfastapi.utilsfastapi.response.custom_orjson_response import ProjectJSONResponse as JsonResponse

from ....utility.setting.global_variable import dict_of_routers_meta_data
from ....session.dependency import check_user_auth
from ... import (
    NAME,
    PERSIAN_NAME,
)
from ...dto.v1 import ModelAdminCreateRequest as RequestModel
from ...dto.v1 import ModelAdminCreateResponseWithSchema as ResponseModel
from ...service.v1 import create_admin as service
from .router import admin_router

ROUTE_NAME = 'create_' + NAME + '_admin'
ROUTE_PERSIAN_NAME = 'ایجاد ' + PERSIAN_NAME
dict_of_routers_meta_data[ROUTE_NAME] = {'persian_name': ROUTE_PERSIAN_NAME}


@admin_router.post(
    path="",
    name=ROUTE_NAME,
    summary='summary',
    description='description',
    response_description='response_description',
    openapi_extra=None,
    response_model=ResponseModel,
    dependencies=[Depends(check_user_auth)]
)
async def create_admin(
        model: RequestModel
) -> JsonResponse:
    data = await service(model=model)
    return JsonResponse(**data.model_dump())
