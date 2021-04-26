from datetime import datetime
import os
from Scrapers.Controller.ScraperController import get_all_prices

if __name__ == '__main__':
    products = get_all_prices()
    current_date = datetime.now().strftime("%m-%d-%Y|%H:%M:%S")
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(THIS_FOLDER, f"PetBedPrices{current_date}.csv")
    file = open(file_name, "w")
    file.write("VENDOR,SIZE,NAME,PRICE,DATA_SOURCE_URL\n")
    for product in products:
        file.write(f'{str(product)}\n')
    file.close()
