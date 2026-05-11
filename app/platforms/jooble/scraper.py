import httpx
import logging
from typing import Any

from app.common.config import JOOBLE_API_KEY
from app.abstract.scrapers import BaseScraper
from app.schemas.pipeline import ScrapingMetadata, ScraperOutputSchema

logger = logging.getLogger("app")


class JoobleScraper(BaseScraper):
    """
    Scraper for the Jooble API to retrieve job vacancies.
    """

    def __init__(self):
        self.base_url = f"https://jooble.org/api/{JOOBLE_API_KEY}"

    async def _fetch_all(self, keyword: str, location: str, limit: int = 100) -> list[dict[str, Any]]:
        """
        Internal method to make HTTP requests to the Jooble API.
        """
        if not JOOBLE_API_KEY:
            logger.error("JOOBLE_API_KEY is missing. Please check your .env file.")
            return []

        payload = {
            "keywords": keyword,
            "location": location,
            "page": "1",
            "ResultOnPage": str(limit)
        }

        logger.info(f"Fetching jobs from Jooble. Keyword: '{keyword}', Location: '{location}'")

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(self.base_url, json=payload)
                response.raise_for_status()

                data = response.json()
                jobs = data.get("jobs", [])

                logger.info(f"Successfully fetched {len(jobs)} jobs. Total available: {data.get('totalCount')}")
                return jobs

            except httpx.HTTPStatusError as e:
                logger.error(f"HTTP error occurred: Status {e.response.status_code} - {e.response.text}")
                return []
            except Exception as e:
                logger.error(f"An unexpected error occurred during API request: {str(e)}")
                return []

    async def scrape(self, metadata: ScrapingMetadata, **kwargs) -> ScraperOutputSchema:
        """
        Main entry point for the scraping process.

        Args:
            metadata: Metadata containing platform and pipeline information.
            **kwargs: Additional parameters.

        Returns:
            ScraperOutputSchema: Object containing the list of raw vacancy data.
        """
        logger.info(f"Starting scraping process for {metadata.platform.value}...")

        raw_items = await self._fetch_all(
            keyword=metadata.keyword,
            location=metadata.location,
            limit=kwargs.get("limit", 100)
        )

        return ScraperOutputSchema(
            metadata=metadata,
            raw_data=raw_items
        )
