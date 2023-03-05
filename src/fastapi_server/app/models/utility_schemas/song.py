"""Pydantic schmata used by 'song' ressources."""
import datetime as dt

from app.models.base import BaseSchema
from pydantic import AnyUrl


class SongOptionalSchema(BaseSchema):
    """Used to query 'children' table against.

    All optional allows to query for every attricbute optionally.
    """

    id: int | None = None
    title: str | None = None
    url: AnyUrl | None = None
    updated_at: dt.datetime | None = None
