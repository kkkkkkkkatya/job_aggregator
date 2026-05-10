from tortoise import fields

from app.infrastructure.database.models.base import AbstractBaseModel


class Skill(AbstractBaseModel):
    """
    Dictionary of technologies (Hard Skills).
    """
    name = fields.CharField(max_length=100, unique=True)
    category = fields.CharField(max_length=50, null=True)

    class Meta:
        table = "skills"
