from typing import Generator

import pytest
from playwright.sync_api import Browser, BrowserContext, Page

from data.constants import DASHBOARD_URL, VALID_PASSWORD, VALID_USERNAME
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


@pytest.fixture(scope="session")
def authenticated_storage_state(browser: Browser) -> dict:
    context = browser.new_context()

    try:
        page = context.new_page()

        login_page = LoginPage(page)
        login_page.open()
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        page.wait_for_url("**/dashboard/index")

        return context.storage_state()

    finally:
        context.close()


@pytest.fixture
def authenticated_context(
    browser: Browser,
    authenticated_storage_state: dict,
) -> Generator[BrowserContext, None, None]:
    context = browser.new_context(storage_state=authenticated_storage_state)

    yield context

    context.close()


@pytest.fixture
def authenticated_page(
    authenticated_context: BrowserContext,
) -> Generator[Page, None, None]:
    page = authenticated_context.new_page()
    page.goto(DASHBOARD_URL)

    yield page

    page.close()


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    login_page = LoginPage(page)
    login_page.open()
    return login_page


@pytest.fixture
def dashboard_page(authenticated_page: Page) -> DashboardPage:
    return DashboardPage(authenticated_page)
