from Scrapers.Utilities.ScraperUtilities import perform_simulated_browser_request


def get_home_depot_price(url: str) -> str:
    soup = perform_simulated_browser_request(url)
    result = soup.find('span', class_='fbtProductLine__price')
    return result.text
