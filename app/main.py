from os import environ

from litestar import Litestar, get
from litestar.logging import LoggingConfig

from app.location import location_router


logging_config = LoggingConfig(
    root={"level": "INFO", "handlers": ["queue_listener"]},
    formatters={
        "standard": {"format": "%(asctime)s %(name)s:%(levelname)s - %(message)s"}
    },
    log_exceptions="always",
)

logger = logging_config.configure()()


@get("/")
async def index() -> str:
    return "Hello, world!"


def init_scheduler(app: Litestar) -> None:
    assert app.logger is not None
    if app.state.get("scheduler") is None:
        app.logger.info("Initializing the scheduler")
    else:
        app.logger.info("Scheduler already initialized")
        return
    app.logger.info("Scheduler initialized")


def on_startup() -> None:
    assert app.logger is not None
    if "GIT_HASH" in environ:
        app.logger.info(f"Running version {environ['GIT_HASH']}")
    else:
        app.logger.warning("No GIT_HASH variable found")
    init_scheduler(app)


app = Litestar(
    [
        index,
        location_router("/location"),
    ],
    on_startup=[on_startup],
    logging_config=logging_config,
)
