import re
from playwright.sync_api import Page, expect
from pages.orengehrm_loginpage import OrangeHRMLoginPage
from pages.orenge_homepage import OrengeHomepage



def test_orengeHrm_example(page: Page) -> None:
    login_page = OrangeHRMLoginPage(page)
    homepage = OrengeHomepage(page)
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", wait_until="domcontentloaded")
    # page.wait_for_timeout(10000)  # Wait for 3 seconds to ensure the page is fully loaded
    login_page.user_name("Admin")
    login_page.password("admin123")
    login_page.click_login()
    expect(page.get_by_role("button", name="Upgrade")).to_be_visible()
    homepage.click_recruitment()
    homepage.click_dashboard()