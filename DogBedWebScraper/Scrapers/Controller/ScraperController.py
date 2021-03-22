import concurrent.futures
import random
import time

from Data.Product import Product
from ProductLinks.ProductsPages import get_tracked_home_depot_products, get_tracked_tractor_supply_co_products, \
    get_tracked_petco_products, get_tracked_walmart_products, get_tracked_chewy_products, get_tracked_wayfair_products
from Scrapers.Websites.ChewyScraper import get_chewy_price
from Scrapers.Websites.HomeDepotScraper import get_home_depot_price
from Scrapers.Websites.PetcoScraper import get_petco_price
from Scrapers.Websites.TractorSupplyCoScraper import get_tractor_supply_co_price
from Scrapers.Websites.WalmartScraper import get_walmart_price
from Scrapers.Websites.WayfairScraper import get_wayfair_price


def get_all_prices():
    all_products = []
    # I am speed (farm each scraped site off to a thread)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_home_depot_prices), executor.submit(get_tractor_supply_prices),
                   executor.submit(get_petco_prices), executor.submit(get_walmart_prices),
                   executor.submit(get_chewy_prices), executor.submit(get_wayfair_prices)]
        for future in concurrent.futures.as_completed(futures):
            if len(future.result()) == 0:
                continue
            else:
                products = future.result()
                # Append all the products
                all_products.extend(products)
                for product in products:
                    print(str(product))
    return all_products


def get_wayfair_prices():
    wayfair_products = []
    tracked_products = get_tracked_wayfair_products()
    for product in tracked_products:
        try:
            # Sleep done within get_wayfair_price
            products = get_wayfair_price(tracked_products[product])
            wayfair_products.extend(products)
        except Exception as e:
            # Want to catch generic exception so report generates anyway (pages change so what works today may not work tomorrow)
            print("WAYFAIR FAILED")
            print(e)
    return wayfair_products


def get_home_depot_prices() -> list[Product]:
    home_depot_products = []
    tracked_products = get_tracked_home_depot_products()
    for product in tracked_products:
        try:
            # Pretend to be human
            time.sleep(random.uniform(3, 10))
            price = get_home_depot_price(tracked_products[product])
            product = Product("Home Depot", product, price, tracked_products[product])
            home_depot_products.append(product)
        except Exception as e:
            # Want to catch generic exception so report generates anyway (pages change so what works today may not work tomorrow)
            print("HOME DEPOT FAILED")
            print(e)
    return home_depot_products


def get_petco_prices() -> list[Product]:
    petco_products = []
    tracked_products = get_tracked_petco_products()
    for tracked_product in tracked_products:
        try:
            # Pretend to be human
            time.sleep(random.uniform(3, 10))
            prices = get_petco_price(tracked_products[tracked_product])
            for price in prices:
                product_name = tracked_products[tracked_product].rsplit('/', 1)[1]
                product = Product('Petco', f'{price}-{product_name}', prices[price], tracked_products[tracked_product])
                petco_products.append(product)
        except Exception as e:
            # Want to catch generic exception so report generates anyway (pages change so what works today may not work tomorrow)
            print("PETCO FAILED")
            print(e)
    return petco_products


def get_walmart_prices() -> list[Product]:
    walmart_products = []
    tracked_products = get_tracked_walmart_products()
    for tracked_product in tracked_products:
        try:
            time.sleep(random.uniform(3, 10))
            price = get_walmart_price(tracked_products[tracked_product])
            product = Product('Walmart', tracked_product, price, tracked_products[tracked_product])
            walmart_products.append(product)
        except Exception as e:
            # Want to catch generic exception so report generates anyway (pages change so what works today may not work tomorrow)
            print("WALMART FAILED")
            print(e)
    return walmart_products


def get_chewy_prices() -> list[Product]:
    chewy_products = []
    tracked_products = get_tracked_chewy_products()
    for tracked_product in tracked_products:
        try:
            time.sleep(random.uniform(3, 10))
            price = get_chewy_price(tracked_products[tracked_product])
            product = Product('Chewy', tracked_product, price, tracked_products[tracked_product])
            chewy_products.append(product)
        except Exception as e:
            # Want to catch generic exception so report generates anyway (pages change so what works today may not work tomorrow)
            print("CHEWY FAILED")
            print(e)
    return chewy_products


def get_tractor_supply_prices() -> list[Product]:
    tractor_supply_products = []
    tracked_products = get_tracked_tractor_supply_co_products()
    for tracked_product in tracked_products:
        try:
            time.sleep(random.uniform(3, 10))
            price = get_tractor_supply_co_price(tracked_products[tracked_product])
            product = Product('Tractor Supply Co.', tracked_product, price, tracked_products[tracked_product])
            tractor_supply_products.append(product)
        except Exception as e:
            # Want to catch generic exception so report generates anyway (pages change so what works today may not work tomorrow)
            print("TRACTOR SUPPLY CO FAILED")
            print(e)
    return tractor_supply_products
