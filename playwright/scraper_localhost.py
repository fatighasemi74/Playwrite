import requests
import logging
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

# def test_adidas(playwright: sync_playwright):
#     context = playwright.request.new_context()
#     response = context.get(url="https://www.adidas.com")

#     assert response.status == 200
#     assert response.status_text == 'OK'

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def test_website():
    with sync_playwright() as p:
        # launch a browser
        browser = p.chromium.launch(headless=False, slow_mo=500)
        # create a new page
        page = browser.new_page()
        base_url = "http://127.0.0.1:8000"

    
        # get all urls in homepage
        response = requests.get(base_url)
        if response.status_code != 200:
            logger.error(f"Failed to retrieve base page with status code {response.status_code}")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')

        unique_urls = set()

        for link in links:
            href = link.get('href')
            if href and not href.startswith("http"):
                full_url = base_url + href if href.startswith('/') else base_url + '/' + href
                unique_urls.add(full_url)
            elif href:
                unique_urls.add(href)

        for url in unique_urls:
            response = page.goto(url)
            if response.status == 200:
                logger.info(f"Successfully visited {url}, status: {response.status}")
            else:
                logger.error(f"Failed to visit {url}, status: {response.status}")
            assert response.status == 200

        browser.close()