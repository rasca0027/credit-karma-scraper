from datetime import date, datetime
from typing import Dict, List
import scraper
from config import Config
from pprint import pprint 
import re 
import csv 

PETAL1 = r"Petal 1"
PETAL2 = r"Petal 2"


def get_card_ranking(card, rankings) -> str:
    ranking =  [item['rank'] for item in rankings if re.search(card, item["card"])]
    return ranking[0] if ranking else 'N/A'

def display_ranking(rankings: list, name:str) -> None:
    print(f'List: {name} =================================== ')
    for item in rankings:
        print(f"{item['rank']} - {item['card']}")

def save(data: List[dict], filename: str) -> None:
    header = list(data[0].keys())
    with open(filename, 'w', encoding='UTF8') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)





if __name__ == "__main__":
    # urls of web pages to scrape
    config = Config()
    petal_rankings = []
    today =  datetime.now().strftime("%m/%d/%Y")
    for item in config.list:
        web_scraper = scraper.determine_scraper(item["url"], item["name"])
        rankings: List[Dict] = web_scraper.get_rankings()
        display_ranking(rankings, item["name"])
        rank = { "date": today,
                 "pate_title" : item["name"], 
                 "p1_rank": get_card_ranking(PETAL1, rankings),
                 "p2_rank": get_card_ranking(PETAL2, rankings),
        }

        petal_rankings.append(rank)
 

    print("PETAL RANKINGS")
    pprint(petal_rankings)
    save(petal_rankings, 'petal_rankings.csv')
