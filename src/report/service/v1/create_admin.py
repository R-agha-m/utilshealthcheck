from ....utility.dto.constance import *
from ....province.database.action import is_one_item_exist_by_pid as province_is_one_item_exist_by_pid
from ...dto.v1 import ModelAdminCreateRequest as RequestModel
from ...dto.v1 import ModelAdminCreateResponseWithSchema as ResponseModel
from ...utility import (
    fetch_x_pid,
    add_image,
)
from ...database.action import (
    is_one_item_absent_by_filter,
    insert_one,
)


async def create_admin(model: RequestModel) -> ResponseModel:
    await is_one_item_absent_by_filter(
        filter_={'name_farsi': model.name_farsi},
        fetch_links=False,
        raise_on_existence=True,
        exception_input={
            'status_code': HTTP_409_CONFLICT,
            'success': False,
            'data': None,
            'error': MESSAGE_DUPLICATE_ITEM_ERROR,
            'message': MESSAGE_DUPLICATE_ITEM_ERROR,
        },
    )

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

    obj = await insert_one(inputs=model.model_dump(exclude={'image'}))

    obj = await add_image(
        image=model.image,
        obj=obj,
    )

    pids_objs = await fetch_x_pid(obj=obj)

    return ResponseModel(
        status_code=HTTP_201_CREATED,
        success=True,
        message=MESSAGE_SUCCESS,
        error=None,
        data={
            **obj.model_dump(),
            **pids_objs,
        },
    )
