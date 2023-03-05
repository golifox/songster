"""Domain Repository for 'artist' entity.

All logic related to the artist entity is defined and grouped here.
"""
from app.db.models.artist import Artist as ArtistModel
from app.db.repositories.base import SQLAlchemyRepository
from app.models.domain.artist import ArtistCreate
from app.models.utility_schemas.artist import ArtistOptionalSchema
from sqlalchemy import select
from sqlalchemy.orm import selectinload


class ArtistRepository(SQLAlchemyRepository):
    """Handle all logic related to artist entity.

    Inheritence from 'SQLAlchemyRepository' allows for
    crud functionality, only schemata and models used have to be defined.
    """

    sqla_model = ArtistModel

    create_schema = ArtistCreate
    read_optional_schema = ArtistOptionalSchema

    async def get_artist_by_name(
        self,
        name: str,
    ) -> sqla_model | None:
        stmt = select(self.sqla_model).filter(self.sqla_model.name == name)
        res = await self.db.execute(statement=stmt)

        artist = res.scalars().first()
        if artist is None:
            return None
        else:
            return artist

    # Testing relationship patterns are working
    async def get_artist_song_by_id(
        self,
        id,
    ) -> list[sqla_model] | None:
        """Get all song belonging to a certain artist."""
        stmt = (
            select(self.sqla_model)
            .options(selectinload(self.sqla_model.songs))
            .filter_by(id=id)
        )

        res = await self.db.execute(stmt)

        artist = res.scalars().first()
        if artist is None:
            return None
        else:
            return artist.songs
