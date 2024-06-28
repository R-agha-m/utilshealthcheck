from utilsfastapi.utilsfastapi.middleware import (
    prepare_cors_middleware,
    prepare_gzip_middleware,
    prepare_process_time_header,
)

from ...fast_api_pre_setup import app
from ...setting import SETTINGS

prepare_cors_middleware(app=app)

prepare_gzip_middleware(
    app=app,
    minimum_size=SETTINGS.GZIP_MIDDLEWARE.MINIMUM_SIZE_IN_BYTE
)

prepare_process_time_header(app=app)

from ...history import middleware  # noqa
