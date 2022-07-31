import sqlalchemy as sa

from .db import base


class Url(base):
    __tablename__ = "urls"
    name = sa.Column(sa.String, primary_key=True)
    url = sa.Column(sa.String)
    views = sa.Column(sa.Integer, default=0)
    active = sa.Column(sa.Boolean, default=True)
