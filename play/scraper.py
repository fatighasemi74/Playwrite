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
        
        base_url = "http://127.0.0.1:8080"
        response = requests.get(base_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            urls = [link.get('href') for link in links if link.get('href') is not None]
            for url in urls:
                main_url = base_url + url
                response = page.goto(main_url)
                print(response)

                assert response.status == 200 
                
        browser.close()