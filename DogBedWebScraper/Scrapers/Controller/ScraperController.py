from Data.Product import Product
from ProductLinks.ProductsPages import get_tracked_home_depot_products, get_tracked_tractor_supply_co_products, \
    get_tracked_petco_products, get_tracked_walmart_products, get_tracked_chewy_products
from Scrapers.Websites.ChewyScraper import get_chewy_price
from Scrapers.Websites.HomeDepotScraper import get_home_depot_price
from Scrapers.Websites.PetcoScraper import get_petco_price
from Scrapers.Websites.TractorSupplyCoScraper import get_tractor_supply_co_price
from Scrapers.Websites.WalmartScraper import get_walmart_price


def get_all_prices():
    all_products = []
    print('Home Depot')
    all_products.extend(get_home_depot_prices())
    # all_products.extend(get_tractor_supply_prices())
    print('Petco')
    all_products.extend(get_petco_prices())
    print('Walmart')
    all_products.extend(get_walmart_prices())
    print('Chewy')
    all_products.extend(get_chewy_prices())
    return all_products


def get_home_depot_prices() -> list[Product]:
    home_depot_products = []
    tracked_products = get_tracked_home_depot_products()
    for product in tracked_products:
        price = get_home_depot_price(tracked_products[product])
        product = Product("Home Depot", product, price, tracked_products[product])
        home_depot_products.append(product)
    return home_depot_products


def get_petco_prices() -> list[Product]:
    petco_products = []
    tracked_products = get_tracked_petco_products()
    for tracked_product in tracked_products:
        prices = get_petco_price(tracked_products[tracked_product])
        for price in prices:
            product_name = tracked_products[tracked_product].rsplit('/', 1)[1]
            product = Product('Petco', f'{price}-{product_name}', prices[price], tracked_products[tracked_product])
            petco_products.append(product)
    return petco_products


def get_walmart_prices() -> list[Product]:
    walmart_products = []
    tracked_products = get_tracked_walmart_products()
    for tracked_product in tracked_products:
        price = get_walmart_price(tracked_products[tracked_product])
        product = Product('Walmart', tracked_product, price, tracked_products[tracked_product])
        walmart_products.append(product)
    return walmart_products


def get_chewy_prices() -> list[Product]:
    chewy_products = []
    tracked_products = get_tracked_chewy_products()
    for tracked_product in tracked_products:
        price = get_chewy_price(tracked_products[tracked_product])
        product = Product('Chewy', tracked_product, price, tracked_products[tracked_product])
        chewy_products.append(product)
    return chewy_products


def get_tractor_supply_prices() -> list[Product]:
    pass
    # tractor_supply_products = []
    # tracked_products = get_tracked_tractor_supply_co_products()
    # for product in tracked_products:
    #     products = get_tractor_supply_co_price(tracked_products[product])
    # return tractor_supply_products
