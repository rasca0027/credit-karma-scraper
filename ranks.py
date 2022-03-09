from typing import Dict, List

import scraper


if __name__ == "__main__":
    # urls of web pages to scrape
    urls = [
        ("https://www.creditkarma.com/credit-cards/student-cards", "Student Cards"),
        ("https://www.creditkarma.com/credit-cards/no-annual-fee", "No Annual Fee"),
        ("https://www.creditkarma.com/credit-cards/fair-credit", "Fair Credit"),
        ("https://www.creditkarma.com/credit-cards/bad-credit", "Bad Credit"),
        ("https://www.creditkarma.com/credit-cards/no-credit", "Limited Credit"),
        ("https://www.creditkarma.com/credit-cards/good-credit", "Good Credit"),
        ("https://www.creditkarma.com/credit-cards/cash-back-cards", "Cash Back Cards"),
        ("https://www.creditkarma.com/credit-cards/rewards-cards", "Rewards"),
    ]

    for url, page_title in urls:
        web_scraper = scraper.determine_scraper(url, page_title)
        rankings: List[Dict] = web_scraper.get_rankings()

        print(rankings)

        # save into file
        # compile csv file.
        # publish
