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
        data = []
        for url in unique_urls:
            response = page.goto(url)

            
            if response.status == 200:
                logger.info(f"Successfully visited {url}, status: {response.status}")
                h3_elements = page.locator('div.shopdesc h3')
                # Evaluate each h3 element to extract the shop name and URL / Javascript function
                shop_entries = h3_elements.evaluate_all('''elements => elements.map(element => {
                    const shopName = element.firstChild.textContent.trim();  // First child assumed to be the text node
                    const shopUrl = element.querySelector('a') ? element.querySelector('a').href : '';  // URL from the <a> tag
                    return { shopName, shopUrl };
                })''')
                for entry in shop_entries:
                    data.append({'Shop Name': entry['shopName'], 'URL': entry['shopUrl']})
                    
                # without Javascript function
                # h3_texts = h3_elements.all_text_contents()
                # for text in h3_texts:
                #     data.append({'Shop Name': text})
            else:
                logger.error(f"Failed to visit {url}, status: {response.status}")
            assert response.status == 200

        browser.close()  

        # Creating DataFrame and save into xlsx file
        df = pd.DataFrame(data)
        df.to_excel('shop_names.xlsx', index=False) 