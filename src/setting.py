from os import sep

from pydantic_settings import (
    SettingsConfigDict,
    BaseSettings,
)
from utilscommon.utilscommon import (
    enum,
    schema,
    base_dir_path_finder,
    add_dir_to_env,
    is_test_mode,
    generate_build_versioning,
)
from utilspreparelogger.utilspreparelogger.prepare_logger import PrepareLogger

from src.utility.setting.schema import (
    Regex,
    Dataset,
    User,
)

# =========================================================================================================== DIRECTORY
BASE_DIR_PATH = base_dir_path_finder(
    file_path=__file__,
    number_of_going_up=2,
)

BASE_DIR_STR = str(BASE_DIR_PATH)

add_dir_to_env(path_=BASE_DIR_STR)


# ============================================================================================================ SETTINGS
class _Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR_STR + sep + "environment_variables",
        env_file_encoding='utf-8',
        env_nested_delimiter='__',
        env_ignore_empty=True,
    )

    GENERAL: schema.SchemaGeneral
    UVICORN_SERVER: schema.SchemaUvicornServer
    LOGGING: schema.SchemaLogging
    MONGODB: schema.SchemaDatabaseWithAuthDb
    MONGODB_TEST: schema.SchemaDatabaseWithAuthDb
    PAGINATION: schema.SchemaPagination
    REGEX: Regex
    OTP: schema.SchemaOtp
    TOKEN: schema.SchemaToken
    GZIP_MIDDLEWARE: schema.SchemaGZipMiddleware
    CACHE: schema.SchemaCache
    PASSWORD: schema.SchemaPassword
    MINIO: schema.SchemaBoto3
    DATASET: Dataset
    KAVEH_NEGAR: schema.SchemaKavehNegar
    USER: User


SETTINGS = _Settings()

# ============================================================================================================ RUN MODE
if is_test_mode():
    RUN_MODE = enum.EnumRunMode.test
else:
    if SETTINGS.GENERAL.IS_PRODUCTION:
        RUN_MODE = enum.EnumRunMode.production

    else:
        RUN_MODE = enum.EnumRunMode.development

# ============================================================================================================== LOGGER
prepare_logger_obj = PrepareLogger(
    project_base_dir=BASE_DIR_STR,
    **SETTINGS.LOGGING.model_dump(by_alias=True),
)
logger = prepare_logger_obj.perform()

# ============================================================================================================= VERSION
VERSION = generate_build_versioning(
    build_file_address=f"{BASE_DIR_STR}{sep}src{sep}utility{sep}setting{sep}buildnumber.version",
    version=SETTINGS.GENERAL.APPLICATION_VERSION,
)

# ============================================================================================================= VERSION
logger.info("Run Mode: %s", RUN_MODE.value)
logger.info("VERSION: %s", VERSION)
