from fastapi import FastAPI

from src.setting import (
    SETTINGS,
    VERSION,
)


# =========================================================================================================== inputs
inputs = {
    "title": SETTINGS.GENERAL.APPLICATION_NAME,
    "description": SETTINGS.GENERAL.APPLICATION_DESCRIPTION,
    "version": VERSION,
}

# ========================================================================================================= create app
app = FastAPI(**inputs)
