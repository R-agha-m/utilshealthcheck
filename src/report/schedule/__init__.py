from pytz import UTC

from ...utility.dto.constance import VARIABLE_MINIO_SCHEDULER_INTERVAL_FOR_DELETE_USELESS_OBJECTS_IN_DAYS
from .delete_useless_objs_from_minio import delete_useless_objs_from_minio

schedules = [
    {
        'func': delete_useless_objs_from_minio,
        'trigger': 'interval',
        'days': VARIABLE_MINIO_SCHEDULER_INTERVAL_FOR_DELETE_USELESS_OBJECTS_IN_DAYS,
        'timezone': UTC
    }
]
