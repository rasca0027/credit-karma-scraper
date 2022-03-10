from typing import Dict, List, Union
import scraper
from config import Config
import re
import csv
import os


class ExportCardRankingsJob:
    """This job will scrap CreditKarma for the Daily Rankings
    and create a csv file with the Petal1 and Petal2 ranking
    on a number of lists that are configured on the config.yml file
    """

    PETAL1 = r"Petal 1"
    PETAL2 = r"Petal 2"

    def __init__(self, dry_run: bool = False) -> None:
        self.dry_run = dry_run

    def _rank(self, card: str, rankings: List[dict]) -> Union[int, None]:
        """returns the rank for a card in a ranking list"""
        ranking = [item["rank"] for item in rankings if re.search(card, item["card"])]
        return ranking[0] if ranking else None

    def _get_card_rankings(self, name: str, url: str) -> List[Dict]:
        """calls the scraper that reads the url and returns the rankings"""
        print("Reading Rankings From", url)
        web_scraper = scraper.determine_scraper(url, name)
        return web_scraper.get_rankings()

    def _save(self, data: List[dict], filename: str) -> None:
        """converts the list of petal rankings into a csv file and saves into a file"""
        self._ensure_dir_exists(filename)
        header = list(data[0].keys())
        with open(filename, "w", encoding="UTF8") as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            writer.writerows(data)

    @staticmethod
    def _ensure_dir_exists(filename: str) -> None:
        os.makedirs(os.path.dirname(filename), exist_ok=True)

    @staticmethod
    def _display_ranking(rankings: list, name: str) -> None:
        """helper method to display the rankings for a list"""
        print(f"List: {name} =================================== ")
        for item in rankings:
            print(f"{item['rank']} - {item['card']}")

    def run(self) -> None:
        config = Config()
        today = config.today

        petal_rankings = []
        for item in config.list:
            rankings = self._get_card_rankings(item["name"], item["url"])
            self._display_ranking(rankings, item["name"])
            record = {
                "date": today,
                "page_title": item["name"],
                "p1_rank": self._rank(self.PETAL1, rankings) or "N/A",
                "p2_rank": self._rank(self.PETAL2, rankings) or "N/A",
            }

            petal_rankings.append(record)

        self._save(petal_rankings, config.outputfile)


if __name__ == "__main__":
    app = ExportCardRankingsJob()
    app.run()
