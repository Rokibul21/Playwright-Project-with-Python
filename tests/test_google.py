import re
from playwright.sync_api import expect

def test_google_search(page):

    page.goto("https://www.google.com/ncr")

    try:
        page.get_by_role("button", name="I agree").click()
    except:
        print("No 'I agree' button found, continuing...")

    page.get_by_role("combobox", name="Search").fill("Playwright Python")
    page.get_by_role("combobox", name="Search").press("Enter")
    page.wait_for_timeout(3000)  # Wait for 3 second to ensure the page is fully loaded

    expect(page).to_have_title(re.compile("Playwright", re.IGNORECASE))

    


