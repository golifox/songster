"""Domain Repository for 'child' entity.

All logic related to the child entity is defined and grouped here.
"""
from app.db.models.song import Song as SongModel
from app.db.repositories.base import SQLAlchemyRepository
from app.models.domain.song import SongCreate
from app.models.utility_schemas.song import SongOptionalSchema


class SongRepository(SQLAlchemyRepository):
    """Handle all logic related to Song entity.

    Inheritence from 'SQLAlchemyRepository' allows for
    crud functionality, only schemata and models used have to be defined.
    """

    sqla_model = SongModel

    create_schema = SongCreate
    read_optional_schema = SongOptionalSchema
