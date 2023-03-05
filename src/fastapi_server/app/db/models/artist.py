"""Sqlalchemy model for 'parent' table.

This is the basic sqlalchemy relationship example 
representing a simple 'ONe-To-Many' relationship pattern.
"""
from app.db.models.base import Base, BaseDBModel
from app.db.models.metadata import metadata_sonsgster
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Artist(Base, BaseDBModel):
    __metadata__ = metadata_sonsgster

    name = Column(String, nullable=False, unique=True, index=True)

    songs = relationship(
        "Song",
        back_populates="author",
        cascade="all, delete-orphan",
    )
