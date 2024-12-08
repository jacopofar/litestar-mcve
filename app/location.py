from datetime import datetime

from litestar import Router, post, Request
from litestar.datastructures import State



@post("/log")
async def log(
    data: dict[str, str], request: Request[None, None, State], headers: dict[str, str]
) -> dict[str, bool]:
    data["received_at"] = datetime.now().isoformat()
    logger = request.app.logger
    logger.info(data)
    assert logger is not None
    logger.info(f"Received log data: {data}")
    return dict(ok=True)


def location_router(path: str) -> Router:
    return Router(path=path, route_handlers=[log])
