import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://github.com/")
    page.get_by_role("link", name="Sign in").click()
    page.get_by_label("Username or email address").click()
    page.get_by_label("Username or email address").fill("fatighasemi74")
    page.get_by_label("Username or email address").press("Tab")
    page.get_by_label("Password").fill("**********")
    page.get_by_role("button", name="Sign in", exact=True).click()
    page.get_by_label("Account menu", exact=True).get_by_label("Close").click()
    page.get_by_label("Account menu", exact=True).get_by_label("Close").click()
    page.get_by_role("button", name="@fatighasemi74 fatighasemi74").click()
    page.get_by_role("button", name="@fatighasemi74 fatighasemi74").click()
    page.get_by_label("Account menu", exact=True).get_by_label("Close").click()
    page.get_by_label("Account menu", exact=True).get_by_label("Close").click()
    page.get_by_label("Global navigation", exact=True).get_by_label("Close").click()
    page.get_by_label("Global navigation", exact=True).get_by_label("Close").click()
    page.get_by_role("heading", name="Top Repositories").click()
    page.get_by_role("button", name="@fatighasemi74 fatighasemi74").click()
    page.get_by_role("button", name="@fatighasemi74 fatighasemi74").click()
    page.get_by_role("button", name="@fatighasemi74 fatighasemi74").click()
    page.get_by_role("button", name="@fatighasemi74 fatighasemi74").click()
    page.get_by_role("button", name="@fatighasemi74 fatighasemi74").click()
    page.get_by_role("button", name="@fatighasemi74 fatighasemi74").click()
    page.get_by_role("button", name="Close").click()
    page.get_by_role("button", name="Close").click()
    page.get_by_role("button", name="Close").click()
    page.get_by_role("link", name="The GitHub Enterprise Server").click()
    page.get_by_role("button", name="Type / to search").click()
    page.get_by_role("link", name="fatighasemi74", exact=True).click()
    page.get_by_role("link", name="DesignPatterns", exact=True).click()
    page.get_by_role("cell", name="singleton.py, (File)").locator("div").first.click()
    page.get_by_role("link", name="singleton.py, (File)").click()
    time.sleep(5)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
