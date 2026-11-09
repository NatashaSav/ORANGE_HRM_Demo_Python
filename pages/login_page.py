from playwright.sync_api import Locator, Page

from data.constants import LOGIN_URL
from data.expected_messages import ExpectedMessages


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")

    def open(self) -> None:
        self.page.goto(LOGIN_URL)

    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_required_messages(self) -> Locator:
        return self.page.get_by_text(ExpectedMessages.REQUIRED)
