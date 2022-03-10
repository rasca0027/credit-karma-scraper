"""Job for Card Rankings from CreditKarma."""
import csv
import os
import re
from typing import Dict
from typing import List
from typing import Union

from config import Config
import scraper


class ExportCardRankingsJob:
    """This job will scrap CreditKarma for the Daily Rankings.

    Create a csv file with the Petal1 and Petal2 ranking
    on a number of lists that are configured on the config.yml file
    """

    PETAL1 = r"Petal 1"
    PETAL2 = r"Petal 2"

    def __init__(self, dry_run: bool = False) -> None:
        self.dry_run = dry_run

    @staticmethod
    def _rank(card: str, rankings: List[dict]) -> Union[int, None]:
        """Returns the rank for a card in a ranking list."""
        ranking = [
            item["rank"] for item in rankings if re.search(card, item["card"])
        ]
        return ranking[0] if ranking else None

    @staticmethod
    def _get_card_rankings(name: str, url: str) -> List[Dict]:
        """Calls the scraper that reads the url and returns the rankings."""
        print("Reading Rankings From", url)
        web_scraper = scraper.determine_scraper(url, name)
        return web_scraper.get_rankings()

    def _save(self, data: List[dict], filename: str) -> None:
        """Converts the list of petal rankings into a csv file and saves into a file."""
        self._ensure_dir_exists(filename)
        header = list(data[0].keys())
        with open(filename, "w", encoding="UTF8") as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            writer.writerows(data)

    @staticmethod
    def _ensure_dir_exists(filename: str) -> None:
        os.makedirs(os.path.dirname(filename), exist_ok=True)

    @staticmethod
    def _display_ranking(rankings: list, name: str) -> None:
        """Helper method to display the rankings for a list."""
        print(f"List: {name} =================================== ")
        for item in rankings:
            print(f"{item['rank']} - {item['card']}")

    def run(self) -> None:
        """Entry point for the job."""
        config = Config()
        today = config.today

        petal_rankings = []

        for item in config.list:
            rankings = self._get_card_rankings(item["name"], item["url"])
            self._display_ranking(rankings, item["name"])
            petal_rankings.append(
                {
                    "date": today,
                    "page_title": item["name"],
                    "p1_rank": self._rank(self.PETAL1, rankings) or "N/A",
                    "p2_rank": self._rank(self.PETAL2, rankings) or "N/A",
                }
            )

        self._save(petal_rankings, config.outputfile)


if __name__ == "__main__":
    app = ExportCardRankingsJob()
    app.run()
