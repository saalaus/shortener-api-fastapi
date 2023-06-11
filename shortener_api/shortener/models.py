import sqlalchemy as sa
from sqlalchemy.orm import relationship, mapped_column

from shortener_api.data.db import base


class Url(base):
    __tablename__ = "urls"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, unique=True)
    url = sa.Column(sa.String)
    views = sa.Column(sa.Integer, default=0)
    active = sa.Column(sa.Boolean, default=True)
