import asyncio
import logging.config

from app.common.config import LOGGER_CONFIG
from app.common.enums import PlatformEnum, PipelineType
from app.schemas.pipeline import ScrapingMetadata
from app.platforms.jooble.scraper import JoobleScraper
from app.infrastructure.database import tortoise_context
from app.infrastructure.database.models.raw_data import RawData

logging.config.dictConfig(LOGGER_CONFIG)
logger = logging.getLogger("app")


async def run_pipeline():
    metadata = ScrapingMetadata(
        platform=PlatformEnum.JOOBLE,
        pipeline_type=PipelineType.VACANCY,
        keyword="Developer",
        location=""
    )

    scraper = JoobleScraper()
    scraper_output = await scraper.scrape(metadata=metadata, limit=2)

    if scraper_output.raw_data:
        logger.info(f"Отримано {len(scraper_output.raw_data)} вакансій. Зберігаємо в БД...")

        saved_count = 0
        skipped_count = 0
        logger.debug(scraper_output.raw_data[0])

        for job_data in scraper_output.raw_data:
            job_link = job_data.get("link")

            if not job_link:
                continue

            record, created = await RawData.get_or_create(
                original_url=job_link,
                defaults={
                    "source_name": scraper_output.metadata.platform.value,
                    "raw_content": job_data,
                    "is_parsed": False
                }
            )

            if created:
                saved_count += 1
            else:
                skipped_count += 1

        logger.info(f"Збереження завершено! Нових додано: {saved_count}, Пропущено дублікатів: {skipped_count}")
    else:
        logger.warning("Дані не знайдено, пропускаємо збереження.")


async def main():
    async with tortoise_context():
        await run_pipeline()


if __name__ == "__main__":
    asyncio.run(main())
