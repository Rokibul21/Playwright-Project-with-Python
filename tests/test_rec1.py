import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://ebs.esquire.com.bd/", wait_until="domcontentloaded")

    page.get_by_role("textbox", name="Employee ID").click()
    page.get_by_role("textbox", name="Employee ID").fill("EC00007439")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("rabby@123")
    page.get_by_role("textbox", name="Password").press("Enter")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("hasan@123")
    page.get_by_role("textbox", name="Password").press("Enter")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="HR").click()
    page.wait_for(state="visible", timeout=10000)
    page.locator("#sidebarnav a").filter(has_text=re.compile(r"^Employee Management$")).click()
    page.get_by_role("tab", name="Incomplete").click()
    with page.expect_popup() as page2_info:
        page.locator("tr:nth-child(3) > td:nth-child(9) > .h4.m-r-10.text-info").click()
    page2 = page2_info.value
    page2.get_by_role("link", name="Esquire Logo").click()
    expect(page2.get_by_role("heading", name="Md. Rokibul Hasan Rabby")).to_be_visible()
    page2.get_by_role("listitem").filter(has_text="Md. Rokibul Hasan Rabby").get_by_role("link").click()
    page2.get_by_role("link", name="   Logout").click()
    page2.goto("https://ebs.esquire.com.bd/")
