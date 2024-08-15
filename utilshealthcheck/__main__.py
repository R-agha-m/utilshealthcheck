print("Acceptable args: --port --appname")

from sys import argv

args = argv[1:]

if len(args) % 2:
    raise ValueError("Args should have an even number of arguments")

COMMAND_CONFIG_DATA = dict()
for index, arg_i in enumerate(args[::2]):
    COMMAND_CONFIG_DATA[arg_i.replace("--", "").lower()] = args[2 * index + 1]


from uvicorn import run

from utilshealthcheck.setting import SETTINGS


if __name__ == "__main__":
    port = COMMAND_CONFIG_DATA.get('port') or SETTINGS.UVICORN_SERVER.PORT

    run(
        app=SETTINGS.UVICORN_SERVER.APP,
        host=SETTINGS.UVICORN_SERVER.HOST,
        port=int(port),
        log_level=SETTINGS.UVICORN_SERVER.LOG_LEVEL.lower(),
        # proxy_headers=SETTINGS.UVICORN_SERVER.PROXY_HEADER,
        forwarded_allow_ips=SETTINGS.UVICORN_SERVER.FORWARDED_ALLOW_IPS,
        reload=SETTINGS.UVICORN_SERVER.RELOAD,
        # loop=SETTINGS.UVICORN_SERVER.LOOP,
        # workers=SETTINGS.UVICORN_SERVER.WORKERS,
        server_header=SETTINGS.UVICORN_SERVER.SERVER_HEADER,
    )
