"""Endpoints for 'Artist' ressource."""
from app.api.dependencies.repository import get_repository
from app.db.repositories.artist import ArtistRepository
from app.models.domain.artist import ArtistCreate, ArtistInDB
from app.models.domain.song import SongInDB
from app.models.utility_schemas.artist import ArtistOptionalSchema
from fastapi import APIRouter, Depends, HTTPException, status
from loguru import logger

router = APIRouter()


# Basic Artist Endpoints
# =========================================================================== #
@router.get(
    "/",
    response_model=list[ArtistInDB],
    name="artist: read-all-artists",
)
async def get_all_artist(
    artist_repo: ArtistRepository = Depends(get_repository(ArtistRepository)),
) -> list[ArtistInDB]:
    artists = await artist_repo.read_all()
    return artists

@router.get(
    "/{id}",
    response_model=ArtistInDB | None,
    name="artist: read-one-Artist",
)
async def get_one_artist(
    id: int,
    artist_repo: ArtistRepository = Depends(get_repository(ArtistRepository)),
) -> ArtistInDB | None:
    artist_db = await artist_repo.read_by_id(id=id)
    if not artist_db:
        logger.warning(f"No Artist with id = {id}.")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No Artist with id = {id}.",
        )

    return artist_db

@router.post(
    "/",
    response_model=ArtistInDB,
    name="artist: create-artist",
    status_code=status.HTTP_201_CREATED,
)
async def post_artist(
    artist_new: ArtistCreate,
    artist_repo: ArtistRepository = Depends(get_repository(ArtistRepository)),
) -> ArtistInDB:
    artist = await artist_repo.get_artist_by_name(artist_new.name)
    if artist:
        error_detail = f"Artist with name {artist.name} already exists"
        logger.warning(error_detail)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error_detail,
        )

    artist = await artist_repo.create(obj_new=artist_new)
    return artist

@router.post(
    "/l",
    name="artist: read-optional-artist",
    response_model=list[ArtistInDB] | None,
)
async def get_optional_artist(
    query_schema: ArtistOptionalSchema,
    artist_repo: ArtistRepository = Depends(get_repository(ArtistRepository)),
) -> list[ArtistInDB] | None:
    artist_db = await artist_repo.read_optional(query_schema=query_schema)
    if not artist_db:
        logger.warning("No artists found.")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No artist matching query: {query_schema.dict(exclude_none=True)}.",
        )

    return artist_db


@router.delete(
    "/{id}", response_model=ArtistInDB, name="artist: delete-Artist"
)
async def delete_artist(
    id: int,
    artist_repo: ArtistRepository = Depends(get_repository(ArtistRepository)),
) -> ArtistInDB:
    artist_deleted = await artist_repo.delete(id=id)
    if not artist_deleted:
        logger.warning(f"No Artist with id = {id}.")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Unable to delete artist with id = {id}, Artist not found",
        )

    return artist_deleted

# Basic relationship pattern endpoint
# =========================================================================== #
@router.get(
    "/{artist_id}/songs",
    name="artist: get-all-song-for-artist",
    response_model=list[SongInDB],
)
async def get_artist_songs(
    id: int,
    artist_repo: ArtistRepository = Depends(get_repository(ArtistRepository)),
) -> list[SongInDB] | None:
    songs = await artist_repo.get_artist_song_by_id(id=id)
    if songs is None:
        logger.info(f"Artist with id: {id} not found.")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Artist with id: {id} not found.",
        )

    if not songs:
        logger.info(f"Artist with id: {id} has no songs.")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No songs found for Artist with with id: {id}.",
        )
    
    return songs

@router.get(
    "/{artist_id}/songs/{song_id}",
    name="artist: get-all-song-for-artist",
    response_model=SongInDB,
)
async def get_artist_song(
    id: int,
    artist_repo: ArtistRepository = Depends(get_repository(ArtistRepository)),
) -> list[SongInDB] | None:
    song = await artist_repo.get_artist_song_by_id(id=id)
    if song is None:
        logger.info(f"Artist with id: {id} not found.")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Artist with id: {id} not found.",
        )

    if not song:
        logger.info(f"Artist with id: {id} has no songs.")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No songs found for Artist with with id: {id}.",
        )

    return song
