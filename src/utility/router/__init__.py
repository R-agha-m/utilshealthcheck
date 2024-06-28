from utilsfastapi.utilsfastapi.router.redirector import router as redirect_router
from utilsfastapi.utilsfastapi.router.cv import router as cv_router

from ...fast_api_pre_setup import app

from ...report.router.v1.router import router

list_of_all_routers = (

    router,

    redirect_router,
    cv_router,
)

for router in list_of_all_routers:
    app.include_router(router)
