from typing import Dict, List
import scraper
from config import Config

if __name__ == "__main__":
    # urls of web pages to scrape
    config = Config()
    
    for item in config.list:
        # web_scraper = scraper.determine_scraper(url, page_title)
        # rankings: List[Dict] = web_scraper.get_rankings()
        print (item["name"])
        # print(rankings)

        # save into file
        # compile csv file.
        # publish
