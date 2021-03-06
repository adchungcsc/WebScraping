import time

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Scrapers.Utilities.ScraperUtilities import click_headless_browser_request


def get_prices_of_colored_bed_by_size(driver, color) -> dict:
    size_drop_down = driver.find_element_by_id('attrValue_1_5_-1017_4099276460824375609')
    size_selector = Select(size_drop_down)
    # Not very clean way of doing this (come back to later)
    try:
        # Click on the small option (will fail if disabled)
        size_selector.select_by_value("S")
        # Select the color option
        print(f"swatch_img_{color}")
        driver.find_element_by_id("swatch_attrValue_2_5_-1017_4099276460824375609").is_enabled()
        item = driver.find_element_by_id(f"swatch_img_1").click()
        pricing_element = driver.find_element_by_id("offerPrice_465506")
        print(pricing_element.text)
    except ElementClickInterceptedException:
        pass
    # try:
    #     size_selector.select_by_value("M")
    # except ElementClickInterceptedException:
    #     pass
    # try:
    #     size_selector.select_by_value("L")
    # except ElementClickInterceptedException:
    #     pass
    return {}



def get_tractor_supply_co_price(url: str) -> str:
    driver = click_headless_browser_request("https://www.tractorsupply.com/tsc/product/coolaroo-large-elevated-pet-bed")
    size_drop_down = driver.find_element_by_id('attrValue_1_5_-1017_4099276460824375609')
    size_selector = Select(size_drop_down)
    # Get the small beds
    driver.save_screenshot("pre.png")
    size_selector.select_by_value("S")
    time.sleep(.5)
    driver.save_screenshot("mid.png")
    time.sleep(.5)
    element = driver.find_element_by_id('Terracotta')
    element.click()
    time.sleep(.5)
    element.click()
    time.sleep(.5)
    driver.save_screenshot("post.png")
    pricing_element = driver.find_element_by_id("stickynav_offerPrice_465506")
    print(pricing_element.text)
    #     print(pricing_element.text)
    # different_colors = driver.find_elements_by_class_name('swatch_img')
    # for bed_color_type in different_colors:
    #     color = bed_color_type.get_property("alt")
    #     driver.save_screenshot("snapshot.png")
    #     actual_button = WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.ID, f"swatch_img_2")))
    #     print(actual_button.get_property("type"))
    #     actual_button.submit()
    #     size_selector.select_by_value("M")
    #     pricing_element = driver.find_element_by_id("offerPrice_465506")
    #     print(pricing_element.text)
        # actual_button.click()
        # color_text = driver.find_element_by_id("selectedcolorText")
        # actual_color = color_text.text.split()[1]
        # print(actual_color)
        # prices = get_prices_of_colored_bed_by_size(driver, actual_color)
        # pricing_element = driver.find_element_by_id("offerPrice_465506")
        # print(pricing_element.text)
    # # Get medium beds
    # size_selector.select_by_value("M")
    #
    # # Get large beds
    # size_selector.select_by_value("L")

    # different_colors = driver.find_elements_by_class_name('swatch_img')
    # for bed_color_type in different_colors:
    #     bed_color_type.g
    return "h"
