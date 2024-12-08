from datetime import datetime

from litestar import Router, post



@post("/log")
async def log(
    data: dict[str, str], headers: dict[str, str]
) -> dict[str, bool]:
    data["received_at"] = datetime.now().isoformat()
    print(data)
    return dict(ok=True)


def location_router(path: str) -> Router:
    return Router(path=path, route_handlers=[log])
