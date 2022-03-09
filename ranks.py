from typing import Dict, List
import scraper
from config import Config
from pprint import pprint
import re

PETAL1 = r"Petal 1"
PETAL2 = r"Petal 2"


def get_card_ranking(card, rankings) -> list:
    return [item for item in rankings if re.search(card, item["card"])]


if __name__ == "__main__":

    # load urls of web pages to scrape
    config = Config()

    for webpage in config.list:
        web_scraper = scraper.determine_scraper(webpage["url"], webpage["name"])
        rankings: List[Dict] = web_scraper.get_rankings()

        print(webpage["name"])
        petal1_ranking = get_card_ranking(PETAL1, rankings)
        petal2_ranking = get_card_ranking(PETAL2, rankings)
        pprint(petal1_ranking)
        pprint(petal2_ranking)

        # save into file
        # compile csv file.
        # publish
