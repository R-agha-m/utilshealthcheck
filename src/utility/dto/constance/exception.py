from utilscommon.exception import ProjectBaseException

from .status_code import *
from .message import *

EXCEPTION_UNACCEPTABLE_FORMAT = ProjectBaseException(
    status_code=HTTP_406_NOT_ACCEPTABLE,
    success=False,
    data=None,
    error=MESSAGE_UNACCEPTABLE_FILE_FORMAT,
    message=MESSAGE_UNACCEPTABLE_FILE_FORMAT,
)

EXCEPTION_ITEM_NOT_FOUND = ProjectBaseException(
    status_code=HTTP_404_NOT_FOUND,
    success=False,
    data=None,
    error=MESSAGE_ITEM_NOT_FOUND,
    message=MESSAGE_ITEM_NOT_FOUND,
    log_this_exc=False,
)

EXCEPTION_UNAUTHORIZED_USER = ProjectBaseException(
    status_code=HTTP_403_FORBIDDEN,
    success=False,
    data=None,
    error=MESSAGE_UNAUTHORIZED_USER,
    message=MESSAGE_UNAUTHORIZED_USER,
)

EXCEPTION_INVALID_PASSWORD = ProjectBaseException(
    status_code=HTTP_400_BAD_REQUEST,
    success=False,
    data=None,
    error=MESSAGE_INVALID_PASSWORD,
    message=MESSAGE_INVALID_PASSWORD,
)

EXCEPTION_NO_PASSWORD = ProjectBaseException(
    status_code=HTTP_400_BAD_REQUEST,
    success=False,
    data=None,
    error=MESSAGE_NO_PASSWORD,
    message=MESSAGE_NO_PASSWORD,
)

EXCEPTION_SERVER_ERROR = ProjectBaseException(
    status_code=HTTP_500_INTERNAL_SERVER_ERROR,
    success=False,
    data=None,
    error=MESSAGE_SERVER_ERROR,
    message=MESSAGE_SERVER_ERROR,
)

EXCEPTION_NOT_ALLOWED = ProjectBaseException(
    status_code=HTTP_403_FORBIDDEN,
    success=False,
    data=None,
    error=MESSAGE_NOT_ALLOWED,
    message=MESSAGE_NOT_ALLOWED,
)

EXCEPTION_INACTIVE_USER = ProjectBaseException(
    status_code=HTTP_403_FORBIDDEN,
    success=False,
    data=None,
    error=MESSAGE_INACTIVE_USER,
    message=MESSAGE_INACTIVE_USER,
)
