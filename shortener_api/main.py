from fastapi import FastAPI

from shortener_api.shortener import register_shortener


def register_all_routers(app: FastAPI) -> None:
    register_shortener(app)


def main() -> FastAPI:
    app = FastAPI()

    register_all_routers(app)

    return app


app = main()
