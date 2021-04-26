import time

from Scrapers.Utilities.ScraperUtilities import perform_simulated_browser_request, click_headless_browser_request


def get_home_depot_price(url: str) -> str:
    driver = click_headless_browser_request(url)
    time.sleep(2)
    price_object = driver.find_element_by_id("standard-price").find_elements_by_tag_name('span')
    currency = price_object[0].text
    dollars = price_object[1].text
    cents = price_object[2].text
    price = f'{currency}{dollars}.{cents}'
    return price


