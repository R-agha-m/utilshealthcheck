from ....utility.dto.constance import *
from ....province.database.action import is_one_item_exist_by_pid as province_is_one_item_exist_by_pid
from ...dto.v1 import ModelAdminUpdatePartiallyRequest as RequestModel
from ...dto.v1 import ModelAdminUpdatePartiallyResponseWithSchema as ResponseModel
from ...utility import fetch_x_pid
from ...storage import upload_fileobj_by_base64_extensionless
from ...database.action import (
    update_one_by_pid_with_return,
    is_one_item_exist_by_pid,
)


async def update_partially_admin(
        pid: int,
        model: RequestModel,
) -> ResponseModel:
    await is_one_item_exist_by_pid(
        pid=pid,
        raise_on_absence=True,
        exception_input={
            'status_code': HTTP_404_NOT_FOUND,
            'success': False,
            'data': None,
            'error': MESSAGE_ITEM_NOT_FOUND,
            'message': MESSAGE_ITEM_NOT_FOUND,
        },
    )

    inputs = model.model_dump(exclude_unset=True)

    if 'province_pid' in inputs:
        await province_is_one_item_exist_by_pid(
            pid=model.province_pid,
            raise_on_absence=True,
            exception_input={
                'status_code': HTTP_404_NOT_FOUND,
                'success': False,
                'data': None,
                'error': MESSAGE_ITEM_NOT_FOUND,
                'message': MESSAGE_ITEM_NOT_FOUND,

            },
        )

    if 'image' in inputs:
        inputs['image'] = upload_fileobj_by_base64_extensionless(
            content=model.image,
            pid=pid,
        )

    obj = await update_one_by_pid_with_return(
        pid=pid,
        inputs=inputs,
    )

    pids_objs = await fetch_x_pid(obj=obj)

    return ResponseModel(
        status_code=HTTP_200_OK,
        success=True,
        message=MESSAGE_SUCCESS,
        error=None,
        data={
            **obj.model_dump(),
            **pids_objs,
        },
    )
