from playwright.sync_api import sync_playwright


def test_website():
    with sync_playwright() as p:
        # launch a browser
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        # create a new page
        page = browser.new_page()
        base_url = "https://jooyak.netlify.app/"
        page.goto(base_url)
        
        # locate a link element with " Suggest it " text
        button = page.get_by_role('button', name="Suggest it")
        button.highlight()
        button.click()

        # Books & Audible
        heading = page.get_by_role('heading', name="Books & Audible")
        heading.highlight()
        heading.click()

        browser.close()    