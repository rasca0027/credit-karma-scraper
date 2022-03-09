from abc import ABC, abstractmethod
from urllib import parse
from typing import List, Dict
import re

from bs4 import BeautifulSoup
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
    def __init__(self, url, page_title):
        super().__init__(url)
        r = requests.get(url)
        self.html = r.text
        self.page_title = page_title

    def get_rankings(self) -> List[Dict]:
        soup = BeautifulSoup(self.html, 'html.parser')
        all_cards = soup.find_all('h3')
        rankings = []
        for i, card in enumerate(all_cards):
            cleaned_card_name = re.sub(r"[^a-zA-Z0-9 ]", "", card.text)
            rankings.append({
                "rank": i + 1,
                "card": cleaned_card_name,
                "source": self.page_title,
            })
        return rankings


def determine_scraper(url: str, page_title: str) -> WebScraper:
    """Determines the website and which scraper to use."""
    domain = parse.urlparse(url).netloc

    if domain == 'www.creditkarma.com':
        return CreditKarmaScraper(url, page_title)

    # We only accepts certain websites now
    raise
