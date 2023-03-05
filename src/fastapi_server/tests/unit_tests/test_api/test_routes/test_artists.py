"""Testing Artist endpoints.

More like unit tests, we're mocking the actual database calls here.
"""
import pytest
from app.db.repositories.artist import ArtistRepository
from app.db.repositories.base import SQLAlchemyRepository
from fastapi import status
from fastapi.encoders import jsonable_encoder


@pytest.mark.anyio
class Test_Artists_Positive:
    """Test class for Artist endpoints."""

    # Basic Artist Endpoints
    # ====================================================================== #
    async def test_create_artist_OK(
        self,
        async_test_client,
        Artist3_Create,
        Artist3_InDB_Schema,
        monkeypatch,
    ):
        # mock the create method that would invoke actual db calls
        async def mock_post(self, obj_new):
            return Artist3_InDB_Schema

        monkeypatch.setattr(SQLAlchemyRepository, "create", mock_post)

        res = await async_test_client.post(
            "/api/artists", json=Artist3_Create
        )

        assert res.status_code == status.HTTP_201_CREATED
        assert res.json() == Artist3_InDB_Schema

    async def test_read_artist_by_id_OK(
        self,
        async_test_client,
        Artist3_InDB_Schema,
        monkeypatch,
    ):
        id: int = 3

        async def mock_read_by_id(self, id):
            return Artist3_InDB_Schema

        monkeypatch.setattr(
            SQLAlchemyRepository, "read_by_id", mock_read_by_id
        )

        res = await async_test_client.get(f"/api/artists/{id}")
        assert res.status_code == status.HTTP_200_OK
        assert res.json() == Artist3_InDB_Schema

    async def test_read_multiple_artists_OK(
        self,
        async_test_client,
        Artist1_InDB_Schema,
        Artist2_InDB_Schema,
        monkeypatch,
    ):
        Artists_in_db = [Artist1_InDB_Schema, Artist2_InDB_Schema]

        async def mock_read_optional(self, query_schema):
            return Artists_in_db

        monkeypatch.setattr(
            SQLAlchemyRepository, "read_optional", mock_read_optional
        )

        res = await async_test_client.get(
            "/api/artists"
        )

        assert res.status_code == status.HTTP_200_OK
        assert res.json() == Artists_in_db

    async def test_delete_artist_OK(
        self,
        async_test_client,
        Artist3_InDB_Schema,
        monkeypatch,
    ):
        id: int = 3

        async def mock_delete(self, id):
            return Artist3_InDB_Schema

        monkeypatch.setattr(SQLAlchemyRepository, "delete", mock_delete)

        res = await async_test_client.delete(f"/api/artists/{id}")

        assert res.status_code == status.HTTP_200_OK
        assert res.json() == Artist3_InDB_Schema

    # Basic relationship pattern endpoint
    # ====================================================================== #
    async def test_get_artist_song_by_id_OK(
        self,
        async_test_client,
        Child1_InDB_Schema,
        Child2_InDB_Schema,
        monkeypatch,
    ):
        children_of_id_1 = [Child1_InDB_Schema, Child2_InDB_Schema]
        params = {"id": 1}

        async def get_Artist_children_by_id(self, id):
            return children_of_id_1

        monkeypatch.setattr(
            ArtistRepository,
            "get_Artist_children_by_id",
            get_Artist_children_by_id,
        )

        res = await async_test_client.get(
            "/api/Artists/get_children", params=params
        )

        assert res.status_code == status.HTTP_200_OK
        assert res.json() == children_of_id_1


@pytest.mark.anyio
class Test_Artists_Negative:
    """Test class for Artist endpoints for negative test cases."""

    # Basic Artist Endpoints
    # ====================================================================== #
    async def test_read_Artist_by_id_NOT_FOUND(
        self,
        async_test_client,
        monkeypatch,
    ):
        params = {"id": 999}

        async def mock_read_by_id(self, id):
            return None

        monkeypatch.setattr(
            SQLAlchemyRepository, "read_by_id", mock_read_by_id
        )

        res = await async_test_client.get(
            "/api/Artists/get_by_id", params=params
        )

        assert res.status_code == status.HTTP_404_NOT_FOUND
        detail = res.json()
        assert res.json() == {"detail": f'No Artist with id = {params["id"]}.'}

    # Basic relationship pattern endpoint
    # ====================================================================== #
    async def test_get_Artist_children_by_id_NOT_FOUND(
        self,
        async_test_client,
        monkeypatch,
    ):
        params = {"id": 999}

        async def mock_get_Artist_children_by_id(self, id):
            return None

        monkeypatch.setattr(
            ArtistRepository,
            "get_Artist_children_by_id",
            mock_get_Artist_children_by_id,
        )

        res = await async_test_client.get(
            "/api/Artists/get_children", params=params
        )

        assert res.status_code == status.HTTP_404_NOT_FOUND
        assert res.json() == {
            "detail": f'Artist with id: {params["id"]} not found.'
        }
