"""Pydantic domain models for 'song' ressource."""
import datetime as dt

from app.models.base import BaseSchema, IDSchemaMixin
from pydantic import AnyUrl


class SongBase(BaseSchema):
    title: str
    url: AnyUrl | None = None
    text: str | None = None
    artist_id: int


class SongCreate(SongBase):
    pass


class SongUpdate(SongBase):
    id: int


class SongInDB(SongBase, IDSchemaMixin):
    updated_at: dt.datetime
