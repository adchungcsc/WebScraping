import random
import time

from Scrapers.Utilities.ScraperUtilities import perform_simulated_browser_request


def get_walmart_price(url: str) -> str:
    soup = perform_simulated_browser_request(url)
    result = soup.find('span', class_='price-group')
    return result.text
