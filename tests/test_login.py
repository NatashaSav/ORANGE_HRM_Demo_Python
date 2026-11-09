import pytest
from playwright.sync_api import Page, expect

from data.constants import (
    DASHBOARD_URL,
    INVALID_PASSWORD,
    INVALID_USERNAME,
    LOGIN_URL,
    VALID_USERNAME,
    VALID_PASSWORD,
    EMPTY_FIELD,
)

from data.expected_messages import ExpectedMessages
from pages.login_page import LoginPage


def test_valid_login(page: Page, login_page: LoginPage):
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    expect(page).to_have_url(DASHBOARD_URL)
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()


@pytest.mark.parametrize(
    "username, password",
    [
        (VALID_USERNAME, INVALID_PASSWORD),
        (INVALID_USERNAME, VALID_PASSWORD),
        (INVALID_USERNAME, INVALID_PASSWORD),
    ],
    ids=[
        "invalid_password",
        "invalid_username",
        "invalid_username_and_password",
    ],
)
def test_login_with_invalid_credentials(
    page: Page, login_page: LoginPage, username: str, password: str
):
    login_page.login(username, password)

    expect(page).to_have_url(LOGIN_URL)
    expect(
        page.get_by_text(ExpectedMessages.INVALID_CREDENTIALS_MESSAGE)
    ).to_be_visible()


@pytest.mark.parametrize(
    "username, password, count_required_messages",
    [
        (EMPTY_FIELD, VALID_PASSWORD, 1),
        (VALID_USERNAME, EMPTY_FIELD, 1),
        (EMPTY_FIELD, EMPTY_FIELD, 2),
    ],
    ids=[
        "empty_username",
        "empty_password",
        "empty_username_and_password",
    ],
)
def test_login_with_empty_fields(
    page: Page,
    login_page: LoginPage,
    username: str,
    password: str,
    count_required_messages: int,
):
    login_page.login(username, password)

    expect(page).to_have_url(LOGIN_URL)
    required_messages = login_page.get_required_messages()
    expect(required_messages).to_have_count(count_required_messages)
    for index in range(count_required_messages):
        expect(required_messages.nth(index)).to_be_visible()
