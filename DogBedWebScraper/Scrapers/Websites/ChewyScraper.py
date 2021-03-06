from Scrapers.Utilities.ScraperUtilities import perform_simulated_rest_request_from_browser


def get_chewy_price(url: str) -> str:
    result = perform_simulated_rest_request_from_browser(url)
    result = result['productComparison']['productComparisonEntries'][0]
    print(f'{result["name"]}, {result["price"][0]["value"]}')
    return f'${result["price"][0]["value"]}'
