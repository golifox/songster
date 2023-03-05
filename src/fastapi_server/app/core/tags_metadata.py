"""Define metadata for tags used in OpenAPI documentation."""
from app.models.base import BaseSchema


## ===== Tags MetaData Schema ===== ##
class ExternalDocs(BaseSchema):
    description: str | None = None
    ulr: str


class MetaDataTag(BaseSchema):
    name: str
    description: str | None = None
    external_docs: ExternalDocs | None = None

    class Config:
        allow_population_by_field_name = True
        fields = {"external_docs": {"alias": "externalDocs"}}


## ===== Tags Metadata Definition ===== ##
artists_tag = MetaDataTag(
    name="artists", description="Example description for artists endpoints."
)

songs_tag = MetaDataTag(
    name="songs",
    description="Stuff that you would want to know about this endpoint.",
)


metadata_tags = [artists_tag, songs_tag]
