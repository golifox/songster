"""Sqlalchemy model for 'song' table.

This is the basic sqlalchemy relationship example 
representing a simple 'ONe-To-Many' relationship pattern.
"""
from app.db.models.base import Base, BaseDBModel
from app.db.models.metadata import metadata_sonsgster
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Song(Base, BaseDBModel):
    __metadata__ = metadata_sonsgster

    title = Column(String, nullable=False, index=True)
    url = Column(String, nullable=True)
    author_id = Column(Integer, ForeignKey("artist.id"))

    author = relationship(
        "Artist",
        back_populates="songs",
    )
