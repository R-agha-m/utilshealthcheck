from datetime import datetime
from csv import DictReader, DictWriter
from io import (
    TextIOWrapper,
    StringIO,
    BytesIO,
)

from fastapi import UploadFile

from ....utility.dto.constance import *
from ...dto.v1 import ModelAdminCreateRequest as RequestModel
from ...dto.v1 import ModelAdminCreateResponse as ResponseModel
from .create_admin import create_admin

FIELDS_NAMES = (
    *ResponseModel.__fields__.keys(),
    'error',
)


async def create_by_file_admin(file: UploadFile):
    if file.content_type == 'text/csv':

        media_type = 'application/csv'
        now = datetime.utcnow().strftime('%Y%m%d-%H%M%S')
        file_name = file.filename.rsplit('.', 1)[0] + f"-Result-{now}.csv"

        reader = DictReader(TextIOWrapper(
            file.file,
            encoding='utf-8-sig',
        ))

        in_memory_file = StringIO()
        writer = DictWriter(
            in_memory_file,
            fieldnames=FIELDS_NAMES,
        )
        writer.writeheader()

        for line in reader:
            try:
                model = RequestModel(**line)
                result = await create_admin(model=model)
                result = result.data.model_dump()

            except Exception as e:
                result = {
                    **line,
                    'error': getattr(e, 'error', None) or str(e),
                }

            writer.writerow(result)

        file_in_string = in_memory_file.getvalue()
        file_in_bytes = bytes(
            file_in_string,
            encoding='utf-8',
        )
        file_in_bytesio = BytesIO(file_in_bytes)

    else:
        raise EXCEPTION_UNACCEPTABLE_FORMAT

    return {
        'media_type': media_type,
        'content': file_in_bytesio,
        'status_code': HTTP_200_OK,
        'headers': {"Content-Disposition": f"attachment; filename={file_name}"},
    }
