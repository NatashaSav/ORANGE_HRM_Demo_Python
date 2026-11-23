import re

from playwright.sync_api import Locator, Page, expect

from data.constants import PIM_PERSONAL_DETAILS_URL
from data.expected_headings import ExpectedHeadings
from data.expected_messages import ExpectedMessages

from pages.components.employee_form import EmployeeForm


class PersonalDetailsPage:
    def __init__(self, page: Page):
        self.page = page
        self.employee_form = EmployeeForm(page)

        self.personal_details_heading: Locator = page.get_by_role(
            "heading", name=ExpectedHeadings.PERSONAL_DETAILS_PAGE_TITLE
        )
        self.employee_full_name: Locator = page.locator(".orangehrm-edit-employee-name")

        self.save_button: Locator = (
            page.locator(".orangehrm-edit-employee-content")
            .locator("form")
            .first.get_by_role("button", name="Save")
        )
        self.success_toast: Locator = page.locator(".oxd-toast--success")

    def save(self) -> None:
        self.save_button.click()

    def verify_personal_details_page(self) -> None:
        expect(self.page).to_have_url(
            re.compile(rf"{PIM_PERSONAL_DETAILS_URL}/empNumber/\d+$")
        )
        expect(self.personal_details_heading).to_have_text(
            ExpectedHeadings.PERSONAL_DETAILS_PAGE_TITLE
        )

    def verify_employee_details(
        self, first_name: str, middle_name: str, last_name: str, employee_id: str
    ) -> None:
        expect(self.employee_full_name).to_have_text(f"{first_name} {last_name}")
        expect(self.employee_form.first_name_input).to_have_value(first_name)
        expect(self.employee_form.middle_name_input).to_have_value(middle_name)
        expect(self.employee_form.last_name_input).to_have_value(last_name)
        expect(self.employee_form.employee_id_input).to_have_value(employee_id)

    def edit_first_name(self, first_name: str) -> None:
        self.employee_form.first_name_input.fill(first_name)

    def click_save_button(self) -> None:
        self.save()

        expect(self.success_toast).to_be_visible()
        expect(self.success_toast).to_contain_text(
            ExpectedMessages.EMPLOYEE_UPDATED_SUCCESSFULLY
        )

    def verify_first_name(self, first_name: str) -> None:
        expect(self.employee_form.first_name_input).to_have_value(first_name)
