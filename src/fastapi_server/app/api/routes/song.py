"""Endpoints for 'song' ressource."""
from app.api.dependencies.repository import get_repository
from app.db.repositories.song import SongRepository
from app.models.domain.song import SongCreate, SongInDB
from app.models.utility_schemas.song import SongOptionalSchema
from fastapi import APIRouter, Depends, HTTPException, status
from loguru import logger

router = APIRouter()


# Basic Parent Endpoints
# =========================================================================== #
@router.get(
    "/songs", 
    response_model=list[SongInDB], 
    name="song: read-all-songs",
)
async def get_all_songs(
    song_repo: SongRepository = Depends(get_repository(SongRepository)),
) -> list[SongInDB]:
    songs = await song_repo.read_all()
    return songs

@router.get(
    "/songs/{id}", 
    response_model=SongInDB | None, 
    name="song: read-one-song-by-id"
)
async def get_one_song(
    id: int,
    song_repo: SongRepository = Depends(get_repository(SongRepository)),
) -> SongInDB | None:
    song_db = await song_repo.read_by_id(id=id)
    if not song_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No song with id = {id}.",
        )

    return song_db

@router.post(
    "/songs",
    response_model=SongCreate,
    name="song: create-Song",
    status_code=status.HTTP_201_CREATED,
)
async def post_song(
    song_new: SongCreate,
    song_repo: SongRepository = Depends(get_repository(SongRepository)),
) -> SongInDB:
    song_created = await song_repo.create(obj_new=song_new)
    return song_created

@router.delete("/songs/{id}", response_model=SongInDB, name="song: delete-song")
async def delete_song(
    id: int,
    song_repo: SongRepository = Depends(get_repository(SongRepository)),
) -> SongInDB:
    song_deleted = await song_repo.delete(id=id)
    if not song_deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Unable to delete song with id = {id}.",
        )

    return song_deleted
