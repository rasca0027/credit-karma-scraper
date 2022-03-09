from typing import Dict, List

import scraper


if __name__ == "__main__":
    # urls of web pages to scrape
    urls = []

    for url in urls:
        rankings: List[Dict] = scraper.determine_scraper(url)
        # list of { rank , card name }

        # save into file
        # compile csv file.
        # publish
