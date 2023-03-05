"""Fixtures for testing 'Song' ressource."""
import datetime as dt

import pytest
from app.db.models.song import Song as SongModel
from app.models.domain.song import SongCreate, SongInDB
from fastapi.encoders import jsonable_encoder


## ===== Valid Song 1 ===== ##
@pytest.fixture
def Song1_Create_Schema() -> SongCreate:
    """Returns a json compatible dict of example SongCreate model"""
    song = SongCreate(
        title="Спокойная ночь",
        url="https://akkords.pro/songs/kino/spokojnaya-noch",
        text="""   Am                              G
                Крыши домов дрожат под тяжестью дней,
                    Dm               Am        
                Небесный пастух  пасет облака,
                Am                             G
                Город стреляет в ночь дробью огней,
                Dm                   Am          
                Но ночь сильней, ее власть велика.""",
        artist_id=1,
    )
    return jsonable_encoder(song)


@pytest.fixture
def Song1_InDB_Schema() -> SongInDB:
    """Returns a json compatible dict of example SongInDB model"""
    UPDATED_AT_DEFAULT = dt.datetime.now()
    Song = SongInDB(
        id=1,
        title="Спокойная ночь",
        url="https://akkords.pro/songs/kino/spokojnaya-noch",
        text="""   Am                              G
                Крыши домов дрожат под тяжестью дней,
                    Dm               Am        
                Небесный пастух  пасет облака,
                Am                             G
                Город стреляет в ночь дробью огней,
                Dm                   Am          
                Но ночь сильней, ее власть велика.""",
        artist_id=1,
        updated_at=UPDATED_AT_DEFAULT,
    )
    return jsonable_encoder(Song)


@pytest.fixture
def Song1_InDB_Model(Song1_InDB_Schema) -> SongModel:
    return SongModel(**Song1_InDB_Schema.dict())


## ===== Valid Song 2 ===== ##
@pytest.fixture
def Song2_Create() -> SongCreate:
    """Returns a json compatible dict of example SongCreate model"""
    Song = SongCreate(
        title="Восьмиклассница",
        url="https://chorder.ru/songs/kino/27-vosmiklassnitsa-akkordy",
        text="""Am        Em
                Пустынной улицей вдвоём
                    C           G
                С тобой куда-то мы идём,
                F          G     C   Am
                Я курю, а ты конфеты ешь.
                    Am        Em
                И светят фонари давно,
                    C             G
                Ты говоришь: "Пойдём в кино",
                F         G      C      Am
                А я тебя зову в кабак, конечно.""",
        artist_id=1,
    )
    return jsonable_encoder(Song)


@pytest.fixture
def Song2_InDB_Schema() -> SongInDB:
    """Returns a json compatible dict of example SongInDB model"""
    UPDATED_AT_DEFAULT = dt.datetime.now()
    Song = SongInDB(
        id=2,
        title="Восьмиклассница",
        url="https://chorder.ru/songs/kino/27-vosmiklassnitsa-akkordy",
        text="""Am        Em
                Пустынной улицей вдвоём
                    C           G
                С тобой куда-то мы идём,
                F          G     C   Am
                Я курю, а ты конфеты ешь.
                    Am        Em
                И светят фонари давно,
                    C             G
                Ты говоришь: "Пойдём в кино",
                F         G      C      Am
                А я тебя зову в кабак, конечно.""",
        updated_at=UPDATED_AT_DEFAULT,
    )
    return jsonable_encoder(Song)


@pytest.fixture
def Song2_InDB_Model(Song2_InDB_Schema) -> SongModel:
    return SongModel(**Song2_InDB_Schema.dict())
