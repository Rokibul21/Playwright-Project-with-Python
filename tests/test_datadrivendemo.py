import csv
import pytest
from playwright.sync_api import Page, expect, TimeoutError as PlaywrightTimeoutError


def get_csv_data() -> list:
    """Read test data from CSV and skip header row."""
    data = []
    with open("./test_data/data.csv", mode="r") as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header if exists
        for row in reader:
            if row:  # skip empty lines
                data.append(row)
    return data

def get_jeson_data() -> list:
    """Read test data from JSON file."""
    import json
    with open("./test_data/data_jeson.jeson", mode="r") as file:
        data = json.load(file)
    return [(item["username"], item["password"]) for item in data]


@pytest.mark.parametrize("username,password", get_jeson_data())
def test_example(page: Page, username, password) -> None:
    try:
        # Navigate to the login page with a higher timeout
        page.goto(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",
            wait_until="domcontentloaded",
            timeout=60000  # 60 seconds
        )

        # Wait for username input to be ready
        page.wait_for_selector('input[name="username"]', timeout=20000)

        # Fill in login form
        page.fill('input[name="username"]', username)
        page.fill('input[name="password"]', password)

        # Click login
        page.click('button[type="submit"]')

        # Expect dashboard to be visible
        expect(page.get_by_role("link", name="Dashboard")).to_be_visible(timeout=20000)

    except PlaywrightTimeoutError as e:
        pytest.fail(f"Test failed due to timeout: {e}")

    except Exception as e:
        pytest.fail(f"Test failed due to an unexpected error: {e}")

    finally:
        # Optional: Add any cleanup code if necessary
        pass
    

def test_invalid_login(page: Page) -> None:
    try:
        page.goto(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",
            wait_until="domcontentloaded",
            timeout=60000  # 60 seconds
        )

        page.wait_for_selector('input[name="username"]', timeout=20000)

        # Fill in invalid login form
        page.fill('input[name="username"]', "InvalidUser")
        page.fill('input[name="password"]', "InvalidPass")

        # Click login
        page.click('button[type="submit"]')

        # Expect error message to be visible
        error_message = page.locator(".oxd-alert-content-text")
        expect(error_message).to_be_visible(timeout=20000)
        expect(error_message).to_have_text("Invalid credentials", timeout=20000)

    except PlaywrightTimeoutError as e:
        pytest.fail(f"Test failed due to timeout: {e}")

    except Exception as e:
        pytest.fail(f"Test failed due to an unexpected error: {e}")

    finally:
        # Optional: Add any cleanup code if necessary
        pass