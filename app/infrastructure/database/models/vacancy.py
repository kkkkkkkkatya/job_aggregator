from tortoise import fields

from app.infrastructure.database.models.base import AbstractBaseModel


class Vacancy(AbstractBaseModel):
    """
    Table for structured and cleaned job postings.
    """
    title = fields.CharField(max_length=255)
    company = fields.CharField(max_length=255, null=True)
    salary_min = fields.IntField(null=True)
    salary_max = fields.IntField(null=True)
    posted_at = fields.DatetimeField(null=True)
    source = fields.CharField(max_length=50)

    skills = fields.ManyToManyField(
        'models.Skill',
        related_name='vacancies',
        through='vacancy_skills'
    )

    class Meta:
        table = "vacancies"
