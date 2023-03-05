"""Bundling of endpoint routers.

Import and add all endpoint routers here.
"""
from app.api.routes import artist, song
from app.core.tags_metadata import artists_tag, songs_tag
from fastapi import APIRouter

router = APIRouter()

router.include_router(
    artist.router, prefix="/artists", tags=[artists_tag.name]
)
router.include_router(song.router, tags=[songs_tag.name])
