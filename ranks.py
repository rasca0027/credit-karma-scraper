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
    # urls of web pages to scrape
    config = Config()
    for item in config.list:
        web_scraper = scraper.determine_scraper(item["url"], item["name"])
        rankings: List[Dict] = web_scraper.get_rankings()
        print (item["name"])
        petal1_ranking = get_card_ranking(PETAL1, rankings)
        petal2_ranking = get_card_ranking(PETAL2, rankings)

        # save into file
        # compile csv file.
        # publish
        pprint(petal1_ranking)
        pprint(petal2_ranking)
