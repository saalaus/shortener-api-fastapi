from pydantic import AnyHttpUrl, BaseModel


class BaseUrl(BaseModel):
    name: str


class CreateUrl(BaseModel):
    url: AnyHttpUrl
    name: str = None


class CreatedUrl(BaseModel):
    shorten_url: AnyHttpUrl


class UpdateUrl(BaseUrl):
    new_name: str = None
    url: AnyHttpUrl = None
    active: bool = None


class DeleteUrl(BaseModel):
    deleted: bool = None

class Url(BaseModel):
    url: AnyHttpUrl
    name: str = None
    active: bool = None
    views: int = None

    class Config:
        orm_mode = True


class HTTPError(BaseModel):
    detail: str

    class Config:
        schema_extra = {
            "example": {"detail": "HTTPException raised."},
        }
