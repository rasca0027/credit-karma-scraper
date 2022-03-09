from abc import ABC, abstractmethod
from urllib import parse

import requests


class WebScraper(ABC):
    """Base abstract class of WebScraper."""

    def __init__(self, url):
        self.url = url

    @abstractmethod
    def get_rankings(self):
        pass


class CreditKarmaScraper(WebScraper):
    """WebScraper class for CreditKarma."""
    def __init__(self, url):
        super().__init__(url)
        r = requests.get(url)
        self.html = r.text

    def get_rankings(self):
        pass


def determine_scraper(url) -> WebScraper:
    """Determines the website and which scraper to use."""
    domain = parse.urlparse(url).netloc

    if domain == 'creditkarma.com':
        return CreditKarmaScraper(url)

    # We only accepts certain websites now
    raise
