from fastapi import APIRouter

from ... import (
    PASCAL_CASE_WITH_SPACE_NAME,
)

router = APIRouter(
    prefix="/report",
    tags=[PASCAL_CASE_WITH_SPACE_NAME],
)
