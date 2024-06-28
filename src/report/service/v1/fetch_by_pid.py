from ....utility.dto.constance import *
from ...dto.v1 import ModelFetchByPidResponseWithSchema as ResponseModel
from ...database.action import (
    fetch_one_by_pid,
    is_one_item_exist_by_pid,
)
from ...utility.fetch_x_pid import fetch_x_pid


async def fetch_by_pid(pid: int) -> ResponseModel:
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

    obj = await fetch_one_by_pid(pid=pid)
    pids_objs = await fetch_x_pid(obj=obj)

    return ResponseModel(
        status_code=HTTP_200_OK,
        success=True,
        message=MESSAGE_SUCCESS,
        error=None,
        data={
            **obj.model_dump(),
            **pids_objs,
        }
    )
