from fastapi import FastAPI
from shortener import register_shortener


def register_all_routers(app):
    register_shortener(app)


def main():
    app = FastAPI()

    register_all_routers(app)

    return app


app = main()
