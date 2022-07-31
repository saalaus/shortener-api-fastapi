from fastapi import FastAPI
from routers.index import register_index


def register_all_routers(app):
    register_index(app)


def main():
    app = FastAPI()

    register_all_routers(app)

    return app


app = main()
