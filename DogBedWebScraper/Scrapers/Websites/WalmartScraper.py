import time

from Scrapers.Utilities.ScraperUtilities import perform_simulated_browser_request, click_headless_browser_request


def get_walmart_price(url: str) -> str:
    driver = click_headless_browser_request(url)
    time.sleep(2)
    price = driver.find_element_by_class_name("price-group").text
    return price
