from typing import Dict, List
import scraper
from config import Config
from pprint import pprint 
import re 

PETAL1 = r"Petal 1"
PETAL2 = r"Petal 2"


def get_card_ranking(card, rankings) -> list:
    return [item['rank'] for item in rankings if re.search(card, item["card"])]

def display_ranking(rankings, name) -> None:
    print(f'List: {name} =================================== ')
    for item in rankings:
        print(f"{item['rank']} - {item['card']}")


if __name__ == "__main__":
    # urls of web pages to scrape
    config = Config()
    petal_rankings = []
    for item in config.list:
        web_scraper = scraper.determine_scraper(item["url"], item["name"])
        rankings: List[Dict] = web_scraper.get_rankings()
        display_ranking(rankings, item["name"])
        rank = { "name" : item["name"], 
                 "petal1": get_card_ranking(PETAL1, rankings),
                "petal2": get_card_ranking(PETAL2, rankings),
        }

        petal_rankings.append(rank)
 

    print("PETAL RANKINGS")
    pprint(petal_rankings)
