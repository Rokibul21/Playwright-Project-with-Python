import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture
def page(context):
    # Start tracing before page creation
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    
    page = context.new_page()
    yield page

    # Stop tracing after test completes
    context.tracing.stop(path="trace.zip")
    page.close()
    context.close()
