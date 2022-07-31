"""Dependancies for FastApi app.

TODO:
    1. do funcs need to be async?
"""
from typing import Callable, Generator, Type

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.db_session import AsyncSessionLocal
from app.db.repositories.base import SQLAlchemyRepository


# DB dependency
async def get_database() -> Generator:
    db = AsyncSessionLocal()
    try:
        yield db
    except:
        # raise Exception here
        pass
    finally:
        await db.close()

    
# Repo dependency
def get_repository(repo_type: Type[SQLAlchemyRepository]) -> Callable:
    def get_repo(
        db: AsyncSession = Depends(get_database),
    ) -> Type[SQLAlchemyRepository]:
        return repo_type(db=db)

    return get_repo

