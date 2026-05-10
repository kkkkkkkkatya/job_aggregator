from tortoise import fields

from app.infrastructure.database.models.base import AbstractBaseModel


class RawData(AbstractBaseModel):
    """
    A table for storing “raw” data from APIs or web scrapers.
    """
    source_name = fields.CharField(max_length=50)
    original_url = fields.CharField(max_length=500, unique=True, null=True)
    raw_content = fields.JSONField()
    is_parsed = fields.BooleanField(default=False)

    class Meta:
        table = "raw_data"
