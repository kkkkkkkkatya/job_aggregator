from typing import Any

from app.schemas.base import BaseSchema
from app.common.enums import PlatformEnum, PipelineType


class ScrapingMetadata(BaseSchema):
    platform: PlatformEnum
    pipeline_type: PipelineType
    keyword: str
    location: str


class ScraperOutputSchema(BaseSchema):
    metadata: ScrapingMetadata
    raw_data: list[dict[str, Any]]


class ParserOutputSchema(BaseSchema):
    metadata: ScrapingMetadata
    raw_data: dict[str, Any]
    parsed_data: dict[str, Any]
    