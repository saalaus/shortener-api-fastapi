from fastapi import FastAPI

from shortener_api.shortener import redirect_router, url_router


def register_all_routers(app: FastAPI) -> None:
    app.include_router(url_router, prefix="/api", tags=["Short URL"])
    app.include_router(redirect_router)


def main() -> FastAPI:
    app = FastAPI(
        title="Url Shortener",
        version="1.0.0",
        description="API for shortener url",
    )

    register_all_routers(app)

    return app


app = main()
