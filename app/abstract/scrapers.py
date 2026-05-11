from abc import ABC, abstractmethod
from app.schemas.pipeline import ScraperOutputSchema, ScrapingMetadata


class BaseScraper(ABC):

    @abstractmethod
    async def scrape(self, metadata: ScrapingMetadata, **kwargs) -> ScraperOutputSchema:
        """Fetch raw platform data and return it wrapped in ScraperOutputSchema."""
        pass
