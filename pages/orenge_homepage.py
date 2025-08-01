
from playwright.sync_api import Page

class OrengeHomepage:
    def __init__(self, page: Page):
        self.page = page
        self.recruitment_link = page.get_by_role("link", name="Recruitment")
        self.dashboard_link = page.get_by_role("link", name="Dashboard")

    def click_recruitment(self):
        self.recruitment_link.click()

    def click_dashboard(self):
        self.dashboard_link.click()