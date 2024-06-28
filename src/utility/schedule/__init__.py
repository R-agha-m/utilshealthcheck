from apscheduler.schedulers.asyncio import AsyncIOScheduler

from ...report.schedule import schedules as city_schedules
from ...dataset.schedule import schedules as dataset_schedules
from ...main_file.schedule import schedules as main_file_schedules
from ...appendix.schedule import schedules as appendix_schedules
from ...organization.schedule import schedules as organization_schedules
from ...province.schedule import schedules as province_schedules
from ...tag.schedule import schedules as tag_schedules
from ...role.schedule import schedules as role_schedules
from ...subject.schedule import schedules as subject_schedules
from ...request.schedule import schedules as request_schedules
from ...subsubject.schedule import schedules as subsubject_schedules
from ...user.schedule import schedules as user_schedules

schedules = [
    *city_schedules,
    *dataset_schedules,
    *organization_schedules,
    *province_schedules,
    *tag_schedules,
    *role_schedules,
    *subject_schedules,
    *request_schedules,
    *subsubject_schedules,
    *user_schedules,
    *appendix_schedules,
    *main_file_schedules,
]

scheduler = AsyncIOScheduler()


async def start_schedule():
    for i in schedules:
        scheduler.add_job(**i)

    scheduler.start()
    return
