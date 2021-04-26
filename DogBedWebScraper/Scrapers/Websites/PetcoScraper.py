import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select

from Scrapers.Utilities.ScraperUtilities import click_headless_browser_request


def get_petco_price(url: str) -> dict:
    prices = {}
    driver = click_headless_browser_request(
        url)
    time.sleep(2)

    # Get the dropdown box
    all_ids = {'Small': '7000000000000003935', 'Medium': '7000000000000005004', 'Large': '7000000000000014927',
               'X-Large': '7000000000000004361'}
    # Find the first available option
    size_selector = Select(driver.find_element_by_class_name('gQOnXn'))
    options = size_selector.options
    frozen_options = []
    # Freeze options (they "change" at runtime)
    for option in options:
        frozen_options.append(option.text)

    for index in range(len(frozen_options)):
        item = frozen_options[index]
        if index == 0:
            size_drop_down = driver.find_element_by_id(all_ids[item])
            size_selector = Select(size_drop_down)
        if item in all_ids:
            try:
                size_selector.select_by_visible_text(item)
                raw_price = driver.find_element_by_class_name("fPOcHS")
                current_price = raw_price.text.split()[0]
                prices[item] = current_price
                size_drop_down = driver.find_element_by_id(all_ids[item])
                size_selector = Select(size_drop_down)
            except NoSuchElementException:
                # size_drop_down = driver.find_element_by_id(all_ids[item])
                print(f'{all_ids[item]} Not Available')
                continue

    return prices
