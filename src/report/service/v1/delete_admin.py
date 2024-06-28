from ....utility.dto.constance import *
from ...dto.v1 import ModelAdminDeleteResponseWithSchema as ResponseModel
from ...database.action import (
    delete_one_by_pid,
    is_one_item_exist_by_pid,
)

RESPONSE_OBJ = ResponseModel(
    status_code=HTTP_200_OK,
    success=True,
    message=MESSAGE_SUCCESS,
    error=None,
    data=None,
)


async def delete_admin(pid: int) -> ResponseModel:
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

    await delete_one_by_pid(pid=pid)
    return RESPONSE_OBJ
