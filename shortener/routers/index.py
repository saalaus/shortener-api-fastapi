from data import schemas
from data.database.crud import create_url, delete_url_by_name, get_url_by_name,\
    update_url_by_name
from data.database.db import get_db
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session


async def url_new(url: schemas.CreateUrl, db: Session = Depends(get_db)):
    url = create_url(db, url.url, url.name)

    return url


async def url_get(url_name: str, db: Session = Depends(get_db)):
    return get_url_by_name(db, url_name)


async def url_update(url: schemas.UpdateUrl, db: Session = Depends(get_db)):
    return update_url_by_name(db, url.name, url.new_name, url.url, url.active)


async def url_delete(url: schemas.BaseUrl, db: Session = Depends(get_db)):
    if delete_url_by_name(db, url.name):
        return {"deleted": True}
    return {"deleted": False}


async def redirect(url: str, db: Session = Depends(get_db)):
    url_obj = get_url_by_name(db, url)
    if url_obj and url_obj.active:
        url_obj.views += 1
        db.commit()
        return RedirectResponse(url_obj.url)
    raise HTTPException(status_code=404, detail="URL not found")


def register_index(app: FastAPI):
    app.add_api_route("/api/url/new", url_new, methods=["POST"],
                      response_model=schemas.Url)
    app.add_api_route("/api/url/get/{url_name}", url_get, methods=["GET"],
                      response_model=schemas.Url)
    app.add_api_route("/api/url/update", url_update, methods=["PATCH"],
                      response_model=schemas.Url)
    app.add_api_route("/api/url/delete", url_delete, methods=["DELETE"])
    app.add_api_route("/{url}", redirect, methods=["GET"])
