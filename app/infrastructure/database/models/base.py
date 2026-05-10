from tortoise import fields
from tortoise.models import Model


class AbstractBaseModel(Model):
    """
    Base Tortoise model inherited by all operational models.
    Uses auto-increment integer PK for simplicity in operational/logging tables.
    """

    id = fields.IntField(pk=True, generated=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        abstract = True
