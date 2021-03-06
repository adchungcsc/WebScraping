import random
import time

from Scrapers.Utilities.ScraperUtilities import perform_simulated_browser_request


def get_walmart_price(url: str) -> str:
    soup = perform_simulated_browser_request(url)
    result = soup.find('span', class_='price-group')
    print(f'walmart {result.text}')
    time.sleep(random.uniform(3, 10))
    return result.text
