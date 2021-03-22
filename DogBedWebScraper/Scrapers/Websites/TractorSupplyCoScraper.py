from Scrapers.Utilities.ScraperUtilities import perform_simulated_rest_request_from_browser


def get_tractor_supply_co_price(url: str) -> str:
    result = perform_simulated_rest_request_from_browser(url)
    catalog_entries = result['catalogEntryView']
    bed = catalog_entries[0]
    bed_price = bed['offer_price_min_10151']
    return bed_price
