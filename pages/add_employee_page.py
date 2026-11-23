import re

from playwright.sync_api import Locator, Page, expect

from data.constants import ADD_EMPLOYEE_URL
from data.expected_headings import ExpectedHeadings
from data.expected_messages import ExpectedMessages

from pages.components.employee_form import EmployeeForm


class AddEmployeePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.employee_form = EmployeeForm(page)

        self.card_container: Locator = page.locator(".orangehrm-card-container")
        self.card_heading: Locator = self.card_container.get_by_role(
            "heading", name=ExpectedHeadings.ADD_EMPLOYEE_PAGE_TITLE
        )

        self.save_button: Locator = page.get_by_role("button", name="Save")
        self.success_toast: Locator = page.locator(".oxd-toast--success")

    def fill_employee_details(
        self, first_name: str, middle_name: str, last_name: str, employee_id: str
    ) -> None:
        self.employee_form.first_name_input.fill(first_name)
        self.employee_form.middle_name_input.fill(middle_name)
        self.employee_form.last_name_input.fill(last_name)
        self.employee_form.employee_id_input.fill(employee_id)

    def save(self) -> None:
        self.save_button.click()

    def verify_add_employee_page(self) -> None:
        expect(self.page).to_have_url(ADD_EMPLOYEE_URL)
        expect(self.card_heading).to_have_text(ExpectedHeadings.ADD_EMPLOYEE_PAGE_TITLE)

    def add_employee(
        self, first_name: str, middle_name: str, last_name: str, employee_id: str
    ) -> None:
        self.fill_employee_details(first_name, middle_name, last_name, employee_id)

        expect(self.employee_form.employee_id_input).to_have_value(employee_id)
        self.save()

        expect(self.success_toast).to_be_visible()
        expect(self.success_toast).to_contain_text(
            ExpectedMessages.EMPLOYEE_SAVED_SUCCESSFULLY
        )
        expect(self.page).to_have_url(
            re.compile(r".*/pim/viewPersonalDetails/empNumber/\d+"),
            timeout=15_000,
        )
