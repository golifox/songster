"""Pydantic schmata used by 'artist' ressources."""
import datetime as dt

from app.models.base import BaseSchema


class ArtistOptionalSchema(BaseSchema):
    """Used to query 'parents' table against.

    All optional allows to query for every attricbute optionally.
    """

    id: int | None
    name: str | None
    updated_at: dt.datetime | None
