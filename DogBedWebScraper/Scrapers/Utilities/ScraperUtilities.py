import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options as ChromeOptions


def perform_simulated_rest_request_from_browser(url: str):
    results = requests.get(url, headers={
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:86.0) Gecko/20100101 Firefox/86.0',
        'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'})
    results = results.json()
    return results


def perform_simulated_browser_request(url: str) -> BeautifulSoup:
    # Might need to randomize the user agent to prevent sites from thinking it's a bot
    http_request_results = requests.get(url, headers={
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:86.0) Gecko/20100101 Firefox/86.0',
        'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
                                        )
    return BeautifulSoup(http_request_results.content, 'html.parser')


def click_headless_browser_request(url: str):
    options = ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/85.0")
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('window-size=1920x1480')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    return driver
