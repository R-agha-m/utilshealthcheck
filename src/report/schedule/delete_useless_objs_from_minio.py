from ...setting import logger
from ..database.action import fetch_list_by_filter
from ..dto.v1 import ProjectionImage
from ..storage import (
    list_objects,
    delete_object,
)
from .. import NAME


async def delete_useless_objs_from_minio() -> None:
    logger.info("Start delete_useless_objs_from_minio for %s", NAME)

    results = await fetch_list_by_filter(
        filter_={'image': {'$ne': None}},
        project_model=ProjectionImage,
    )

    images_exist_in_db = {i.image for i in results}

    minio_objs = list_objects()

    if 'Contents' not in minio_objs:
        return

    images_exist_in_storage = {i['Key'] for i in minio_objs['Contents']}

    images_should_be_deleted = images_exist_in_storage - images_exist_in_db

    for key in images_should_be_deleted:
        try:
            delete_object(key=key)

        except Exception:
            logger.warning("Cannot delete this extra key from storage: %s", key)

    return None
