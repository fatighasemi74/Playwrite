import requests
import json
import logging
import pandas as pd
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def test_website():
    with sync_playwright() as p:
        # launch a browser
        browser = p.chromium.launch(headless=True)
        # create a new page
        page = browser.new_page()
        base_url = "https://www.shopsafe.co.uk"
        
        # get all urls in homepage
        response = requests.get(base_url)
        if response.status_code != 200:
            logger.error(f"Failed to retrieve base page with status code {response.status_code}")
            return
        page.goto(f"{base_url}/shops-a-z")


        links_elements = page.query_selector_all('a.alphabet')
        unique_urls = set()

        for link in links_elements:
            href = link.get_attribute('href')
            if href and not href.startswith("http"):
                full_url = base_url + href if href.startswith('/') else base_url + '/' + href
                unique_urls.add(full_url)
            elif href:
                unique_urls.add(href)
        data = []
        for url in unique_urls:
            page.goto(url)
            shop_elements = page.locator('div.shopdesc h3')
            count = shop_elements.count()

            for i in range(count):
                # Extract the shop name
                shop_name = shop_elements.nth(i).text_content().strip() if shop_elements.nth(i) else ""
                # Assuming the link is within the same h3 element
                shop_url = shop_elements.nth(i).locator('a').get_attribute('href') if shop_elements.nth(i).locator('a') else ""
                data.append({'Shop name': shop_name, 'URL': shop_url})


        browser.close()

        # Creating DataFrame and save into xlsx file
        df = pd.DataFrame(data)
        df.to_excel('shop_names.xlsx', index=False) 
