"""Fixtures for testing 'Artist' ressource."""
import datetime as dt
from typing import List

import pytest
from app.db.models.artist import Artist as ArtistModel
from app.models.domain.artist import ArtistCreate, ArtistInDB
from fastapi.encoders import jsonable_encoder


## ===== Valid Artist 1 ===== ##
@pytest.fixture
def Artist1_Create() -> ArtistCreate:
    """Returns a json compatible dict of example ArtistCreate model"""
    Artist = ArtistCreate(
        name="Кино",
    )
    return jsonable_encoder(Artist)


@pytest.fixture
def Artist1_InDB_Schema() -> ArtistCreate:
    """Returns a json compatible dict of example ArtistInDB model"""
    UPDATED_AT_DEFAULT = dt.datetime.now()
    Artist = ArtistInDB(
        id=1,
        name="Кино",
        updated_at=UPDATED_AT_DEFAULT,
    )
    return jsonable_encoder(Artist)


@pytest.fixture
def Artist1_InDB_Model(Artist1_InDB_Schema) -> ArtistModel:
    return ArtistModel(**Artist1_InDB_Schema.dict())


## ====== Valid Artist 2 ===== ##
@pytest.fixture
def Artist2_Create() -> ArtistCreate:
    """Returns a json compatible dict of example ArtistCreate model"""
    Artist = ArtistCreate(
        name="Король и Шут",
    )
    return jsonable_encoder(Artist)


@pytest.fixture
def Artist2_InDB_Schema() -> ArtistCreate:
    """Returns a json compatible dict of example ArtistInDB model"""
    UPDATED_AT_DEFAULT = dt.datetime.now()
    Artist = ArtistInDB(
        id=2,
        name="Король и Шут",
        updated_at=UPDATED_AT_DEFAULT,
    )
    return jsonable_encoder(Artist)


@pytest.fixture
def Artist2_InDB_Model(Artist2_InDB_Schema) -> ArtistModel:
    return ArtistModel(**Artist2_InDB_Schema.dict())


## ====== Valid Artist 3 ===== ##
@pytest.fixture
def Artist3_Create() -> ArtistCreate:
    """Returns a json compatible dict of example ArtistCreate model"""
    Artist = ArtistCreate(
        name="Найк Борзов",
    )
    return jsonable_encoder(Artist)


@pytest.fixture
def Artist3_InDB_Schema() -> ArtistCreate:
    """Returns a json compatible dict of example ArtistInDB model"""
    UPDATED_AT_DEFAULT = dt.datetime.now()
    Artist = ArtistInDB(
        id=3,
        name="Найк Борзов",
        updated_at=UPDATED_AT_DEFAULT,
    )
    return jsonable_encoder(Artist)


@pytest.fixture
def Artist3_InDB_Model(Artist3_InDB_Schema) -> ArtistModel:
    return ArtistModel(**Artist3_InDB_Schema.dict())
