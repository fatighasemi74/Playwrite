from playwright.sync_api import sync_playwright
import requests
from bs4 import BeautifulSoup

# def test_adidas(playwright: sync_playwright):
#     context = playwright.request.new_context()
#     response = context.get(url="https://www.adidas.com")

#     assert response.status == 200
#     assert response.status_text == 'OK'


def test_website():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        base_url = "http://127.0.0.1:8000"
        response = requests.get(base_url)
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
            print(f"Visited {url}, status: {response.status}")
            # urls = [link.get('href') for link in links if link.get('href') is not None]

            assert response.status == 200 

        browser.close()