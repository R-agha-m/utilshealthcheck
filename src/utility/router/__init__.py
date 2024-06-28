from utilsfastapi.utilsfastapi.router.redirector import router as redirect_router
from utilsfastapi.utilsfastapi.router.cv import router as cv_router

from ...fast_api_pre_setup import app

from ...user.router.v1.router import router as user_router
from ...user.router.v1.router import admin_router as user_admin_router

from ...session.router.v1.router import router as session_router

from ...post.router.v1.router import router as post_router
from ...post.router.v1.router import admin_router as post_admin_router

from ...province.router.v1.router import router as province_router
from ...province.router.v1.router import admin_router as province_admin_router

from ...report.router.v1.router import router as city_router
from ...report.router.v1.router import admin_router as city_admin_router

from ...subject.router.v1.router import router as subject_router
from ...subject.router.v1.router import admin_router as subject_admin_router

from ...request.router.v1.router import router as request_router
from ...request.router.v1.router import admin_router as request_admin_router

from ...subsubject.router.v1.router import router as subsubject_router
from ...subsubject.router.v1.router import admin_router as subsubject_admin_router

from ...organization.router.v1.router import router as organization_router
from ...organization.router.v1.router import admin_router as organization_admin_router

from ...history.router.v1.router import router as history_router
from ...history.router.v1.router import admin_router as history_admin_router

from ...tag.router.v1.router import router as tag_router
from ...tag.router.v1.router import admin_router as tag_admin_router

from ...dataset.router.v1.router import router as dataset_router
from ...dataset.router.v1.router import admin_router as dataset_admin_router

from ...main_file.router.v1.router import router as main_file_router
from ...main_file.router.v1.router import admin_router as main_file_admin_router

from ...appendix.router.v1.router import router as appendix_router
from ...appendix.router.v1.router import admin_router as appendix_admin_router

from ...news.router.v1.router import router as news_router

from ...role.router.v1.router import admin_router as role_admin_router

list_of_all_routers = (

    appendix_router,
    appendix_admin_router,

    city_router,
    city_admin_router,

    dataset_router,
    dataset_admin_router,

    history_router,
    history_admin_router,

    main_file_router,
    main_file_admin_router,

    news_router,

    organization_router,
    organization_admin_router,

    post_router,
    post_admin_router,

    province_router,
    province_admin_router,

    request_router,
    request_admin_router,

    role_admin_router,

    session_router,

    subject_router,
    subject_admin_router,

    subsubject_router,
    subsubject_admin_router,

    tag_router,
    tag_admin_router,

    user_router,
    user_admin_router,

    redirect_router,
    cv_router,
)

for router in list_of_all_routers:
    app.include_router(router)
