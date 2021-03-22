import random
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Data.Product import Product
from Scrapers.Utilities.ScraperUtilities import click_headless_browser_request


def get_wayfair_price(url: str) -> [Product]:
    products = []
    # Initiate session with wayfair as a "normal" customer. this WON'T work if you go to each individual product page due to anti-scraping
    driver = click_headless_browser_request(url)
    # Must be done in the same browser session to fool the anti web scraping function (Needed to hard code these here)
    urls = {
        "Medium Terracotta": "https://www.wayfair.com/pet/pdp/coolaroo-elevated-indooroutdoor-pet-cot-clr1395.html?piid=28102246%2C28102249",
        "Large Terracotta": "https://www.wayfair.com/pet/pdp/coolaroo-elevated-indooroutdoor-pet-cot-clr1395.html?piid=28102246%2C28102248",
        "Medium Brunswick Green": "https://www.wayfair.com/pet/pdp/coolaroo-elevated-indooroutdoor-pet-cot-clr1395.html?piid=28102245%2C28102249",
        "Large Brunswick Green": "https://www.wayfair.com/pet/pdp/coolaroo-elevated-indooroutdoor-pet-cot-clr1395.html?piid=28102245%2C28102248",
        "Medium Gray": "https://www.wayfair.com/pet/pdp/coolaroo-elevated-indooroutdoor-pet-cot-clr1395.html?piid=28102247%2C28102249",
        "Large Gray": "https://www.wayfair.com/pet/pdp/coolaroo-elevated-indooroutdoor-pet-cot-clr1395.html?piid=28102247%2C28102248"
    }
    for url in urls:
        driver.get(urls[url])
        price = driver.find_element_by_class_name("notranslate").text
        product = Product("Wayfair", f"{url} {'Medium' if 'Medium' in url else 'Large'} Elevated Pet Cot", price, urls[url])
        products.append(product)
        # Act natural. Totally not a robot
        time.sleep(random.uniform(3, 10))
    return products
