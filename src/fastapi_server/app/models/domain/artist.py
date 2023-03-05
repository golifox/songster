"""Pydantic domain models for 'artist' ressource."""
import datetime as dt

from app.models.base import BaseSchema, IDSchemaMixin
from app.models.domain.song import SongBase


class ArtistBase(BaseSchema):
    name: str


class ArtistSchema(ArtistBase):
    songs: list[SongBase] | None = []


class ArtistCreate(ArtistBase):
    pass


class ArtistUpdate(ArtistBase):
    pass


class ArtistInDB(ArtistBase, IDSchemaMixin):
    updated_at: dt.datetime
