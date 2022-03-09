from typing import Dict, List
import scraper
from config import Config
from pprint import pprint 

if __name__ == "__main__":
    # urls of web pages to scrape
    config = Config()
    for item in config.list:
        web_scraper = scraper.determine_scraper(item["url"], item["name"])
        rankings: List[Dict] = web_scraper.get_rankings()
        pprint(rankings)

        # save into file
        # compile csv file.
        # publish
