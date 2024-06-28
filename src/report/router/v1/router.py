from fastapi import APIRouter

from ....utility.dto.constance import *
from ... import (
    CAMEL_CASE_NAME,
    PASCAL_CASE_WITH_SPACE_NAME,
)

router = APIRouter(
    prefix=VARIABLE_PATH_V1_CLIENT_PREFIX + CAMEL_CASE_NAME,
    tags=[VARIABLE_TAG_CLIENT + PASCAL_CASE_WITH_SPACE_NAME],
)

admin_router = APIRouter(
    prefix=VARIABLE_PATH_V1_ADMIN_PREFIX + CAMEL_CASE_NAME,
    tags=[VARIABLE_TAG_ADMIN + PASCAL_CASE_WITH_SPACE_NAME],
)
