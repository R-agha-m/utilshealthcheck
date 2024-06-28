from ....utility.dto.constance import *
from ...dto.v1 import ModelAdminFetchByFilterResponseWithSchema as ResponseModel
from ...database.action import fetch_list_by_filter_preparation_with_pagination
from ...utility.fetch_x_pid import fetch_x_pid


async def fetch_by_filter_admin(
        current_page: int,
        page_size: int,
        order_by: dict | None,

        **kwargs,
) -> ResponseModel:
    result = await fetch_list_by_filter_preparation_with_pagination(
        inputs=kwargs,
        current_page=current_page,
        page_size=page_size,
        order_by=order_by,
    )

    prepared_data_list = list()
    for obj in result['data']:
        prepared_data = obj.model_dump()

        pids_objs = await fetch_x_pid(obj=obj)
        prepared_data.update(pids_objs)

        prepared_data_list.append(prepared_data)

    return ResponseModel(
        status_code=HTTP_200_OK,
        success=True,
        message=MESSAGE_SUCCESS,
        error=None,
        data={
            "pagination": result["pagination"],
            'data': prepared_data_list,
        },
    )
