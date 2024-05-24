import requests
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
        page.goto(base_url)
        # get all urls in homepage
        response = requests.get(base_url + "/shops-a-z")
        if response.status_code != 200:
            logger.error(f"Failed to retrieve base page with status code {response.status_code}")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', class_="alphabet")
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
            data = []
            if response.status == 200:
                logger.info(f"Successfully visited {url}, status: {response.status}")
                h3_elements = page.locator('div.shopdesc h3')
                h3_texts = h3_elements.all_text_contents()
                for text in h3_texts:
                    
                    data.append({'URL': url, 'Shop Name': text})
                    # data.append({'Shop Name': text})
            else:
                logger.error(f"Failed to visit {url}, status: {response.status}")
            assert response.status == 200
            # Creating DataFrame
        df = pd.DataFrame(data)
    
        # Saving to Excel
        df.to_excel('shop_names.xlsx', index=False)


        browser.close()    