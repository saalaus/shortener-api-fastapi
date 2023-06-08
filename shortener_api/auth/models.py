import sqlalchemy as sa

from shortener_api.data.db import base


class User(base):
    __tablename__ = "users"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
