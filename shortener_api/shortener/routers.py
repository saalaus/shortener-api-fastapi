from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from shortener_api.data.db import get_db

from . import schemas
from .crud import (
    create_url,
    delete_url_by_name,
    get_url_by_name,
    update_url_by_name,
)

url_router = APIRouter(prefix="/url")
redirect_router = APIRouter()


@url_router.post(
    "/new",
    response_model=schemas.CreatedUrl,
    status_code=status.HTTP_201_CREATED,
    description="Short the url",
    responses={
        status.HTTP_201_CREATED: {
            "model": schemas.CreatedUrl,
            "description": "Short url",
        },
    },
)
async def url_new(
    request: Request,
    url: schemas.CreateUrl,
    db: Session = Depends(get_db),
) -> schemas.CreatedUrl:
    url = create_url(db, url.url, url.name)

    return {"shorten_url": str(request.url_for("redirect", url_name=url.name))}


@url_router.get(
    "/get/{url_name}",
    response_model=schemas.Url,
    status_code=status.HTTP_200_OK,
    description="Get shorten url info",
    responses={
        status.HTTP_200_OK: {
            "model": schemas.Url,
            "description": "Ok response",
        },
    },
)
async def url_get(url_name: str, db: Session = Depends(get_db)) -> schemas.Url:
    return get_url_by_name(db, url_name)


@url_router.patch(
    "/update",
    response_model=schemas.UpdateUrl,
)
async def url_update(
    url: schemas.UpdateUrl,
    db: Session = Depends(get_db),
) -> schemas.Url:
    return update_url_by_name(db, url.name, url.new_name, url.url, url.active)


@url_router.delete(
    "/delete",
    response_model=schemas.DeleteUrl,
)
async def url_delete(
    url: schemas.BaseUrl,
    db: Session = Depends(get_db),
) -> schemas.DeleteUrl:
    if delete_url_by_name(db, url.name):
        return schemas.DeleteUrl(deleted=True)
    return schemas.DeleteUrl(deleted=False)


@redirect_router.get(
    "/{url_name}",
    status_code=status.HTTP_307_TEMPORARY_REDIRECT,
    response_class=RedirectResponse,
    description="Redirect to original url",
    name="redirect",
    responses={
        status.HTTP_307_TEMPORARY_REDIRECT: {
            "description": "Successfull redirect",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Error: url nor found",
            "model": schemas.HTTPError,
        },
    },
)
async def redirect(
    url_name: str,
    db: Session = Depends(get_db),
) -> RedirectResponse:
    url_obj = get_url_by_name(db, url_name)

    if url_obj and url_obj.active:
        url_obj.views += 1
        db.commit()
        return RedirectResponse(url_obj.url)
    raise HTTPException(status_code=404, detail="URL not found")
