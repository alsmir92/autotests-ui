import pytest  # Импортируем pytest
from playwright.sync_api import Page, Playwright


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    # Запускаем браузер
    browser = playwright.chromium.launch(headless=False)
    # Передаем страницу для использования в тесте
    yield browser.new_page()
    browser.close()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto = ("https://nikita-filonov.github.io/qa-automation-engineer-ui"
                 "-course/#/auth/registration")

    email_input = page.get_by_test_id(
        "registration-form-email-input").locator('input')
    email_input.fill("user,name@gmail.com")
