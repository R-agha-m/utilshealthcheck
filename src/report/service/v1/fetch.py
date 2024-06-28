from traceback import format_exc

from fastapi import Request

from __main__ import COMMAND_CONFIG_DATA

from ....utility.dto.constance import *


async def fetch(request: Request) -> dict:
    try:
        results = {
            'status_code': HTTP_200_OK,
            'success': True,
            'message': MESSAGE_SUCCESS,
            'error': None,
            'data': {
                **COMMAND_CONFIG_DATA,
                'headers': {key: value for key, value in request.headers.items()},
                "method": request.method,
                "path_params": request.path_params,
                "query_string": request.query_params,
                'protocol': request.scope['type'],
                'http_version': request.scope['http_version'],
                'path': request.scope['path'],
                'ip:port': f'{request.client.host}:{request.client.port}',
            }
        }
    except Exception:
        results = {
            'status_code': HTTP_500_INTERNAL_SERVER_ERROR,
            'success': True,
            'message': MESSAGE_FAILURE,
            'error': format_exc(),
            'data': None,
        }

    return results
