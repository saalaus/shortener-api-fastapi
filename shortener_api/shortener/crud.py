from slugify import slugify
from sqlalchemy.orm import Session

from shortener_api.utils.random_slug import generate_slug

from .models import Url


def create_url(session: Session, url: str, name: str = None) -> Url:
    if not name:
        name = generate_slug()
    url_obj = Url(url=url, name=slugify(name))
    session.add(url_obj)
    session.commit()
    session.refresh(url_obj)
    return url_obj


def get_url_by_name(session: Session, name: str) -> Url:
    return session.query(Url).filter(Url.name == name).first()


def delete_url_by_name(session: Session, name: str) -> bool:
    query = session.query(Url).filter(Url.name == name).delete()
    session.commit()
    return query


def update_url_by_name(session: Session, name: str, new_name: str = None,
                       url: str = None, active: bool = None) -> Url:
    url_obj = get_url_by_name(session, name)
    if url is not None:
        url_obj.url = url
    if active is not None:
        url_obj.active = active
    if new_name is not None:
        url_obj.name = slugify(new_name)
    session.commit()
    session.refresh(url_obj)
    return url_obj
