from Scrapers.Controller.ScraperController import get_all_prices

if __name__ == '__main__':
    products = get_all_prices()
    f = open("prices.csv", "w")
    for product in products:
        f.write(str(product))
    f.close()
