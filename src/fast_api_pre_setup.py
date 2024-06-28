from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.setting import (
    RUN_MODE,
    SETTINGS,
    enum,
    VERSION,
)
from src.utility.database.engine import init_beanie
from src.utility.database.fixture import import_fixture
from src.utility.schedule import start_schedule


# =========================================================================================================== lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_beanie()

    if RUN_MODE != enum.EnumRunMode.test:
        await import_fixture()

    await start_schedule()
    yield


# =========================================================================================================== inputs
inputs = {
    "title": SETTINGS.GENERAL.APPLICATION_NAME,
    "description": SETTINGS.GENERAL.APPLICATION_DESCRIPTION,
    "version": VERSION,
    'lifespan': lifespan,
}

# if RUN_MODE == enum.EnumRunMode.production:
#     inputs["docs_url"] = None
#     inputs["redoc_url"] = None
#     inputs["openapi_url"] = None

# ========================================================================================================= create app
app = FastAPI(**inputs)
