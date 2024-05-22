from playwright.sync_api import sync_playwright


def test_website():
    with sync_playwright() as p:
        # launch a browser
        browser = p.chromium.launch(headless=False, slow_mo=500)
        # create a new page
        page = browser.new_page()
        base_url = "https://jooyak.netlify.app/"

        # locate a link element with "Blogg" text
        page.goto(base_url)
        # shop_button = page.get_by_role('link', name="Blogg")
        # shop_button.click()

        browser.close()    