import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://ebs.esquire.com.bd/")
    page.get_by_role("textbox", name="Employee ID").click()
    page.get_by_role("textbox", name="Employee ID").fill("EC00007439")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("hasan@123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name=" HR").click()
    page.locator("#sidebarnav a").filter(has_text=re.compile(r"^Employee Management$")).click()
    page.get_by_role("listitem").filter(has_text="Md. Rokibul Hasan Rabby").get_by_role("link").click()
    page.get_by_role("link", name="   Logout").click()
    page.goto("https://ebs.esquire.com.bd/")
    expect(page.get_by_role("link", name="© Esquire Technology Ltd")).to_be_visible()
