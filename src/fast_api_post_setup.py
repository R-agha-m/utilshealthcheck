from utilscommon.utilscommon import EnumRunMode


from src.setting import RUN_MODE
from src.fast_api_pre_setup import app # noqa - need for server
from src.utility import router  # noqa - add routers
from src.utility import exception_handling  # noqa - add exception handlers
from src.utility import middleware  # noqa - add middlewares

if RUN_MODE != EnumRunMode.test:
    from src.utility.database import post_fixture  # noqa - run post fixtures
