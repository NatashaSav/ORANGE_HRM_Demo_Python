from playwright.sync_api import Locator, Page, expect

from data.constants import PIM_URL
from data.expected_menu_items import ExpectedMenuItems

from data.expected_messages import ExpectedMessages
from pages.add_employee_page import AddEmployeePage

from utils.data_generator import (
    generate_first_name,
    generate_last_name,
    generate_middle_name,
    generate_employee_id,
)


class PIMPage:
    EDIT_BUTTON_ICON_SELECTOR = ".bi-pencil-fill"
    DELETE_BUTTON_ICON_SELECTOR = ".bi-trash"

    def __init__(self, page: Page) -> None:
        self.page = page

        self.pim_menu: Locator = page.get_by_role("link", name=ExpectedMenuItems.PIM)
        self.pim_heading: Locator = page.get_by_role(
            "heading", name=ExpectedMenuItems.PIM
        )
        self.header_container: Locator = page.locator(".orangehrm-header-container")
        self.employee_table: Locator = page.locator(".orangehrm-employee-list")
        self.employee_input_group: Locator = page.locator(".oxd-input-group")
        self.employee_name_input: Locator = self.employee_input_group.filter(
            has_text="Employee Name"
        ).locator("input")
        self.employee_id_input: Locator = self.employee_input_group.filter(
            has_text="Employee Id"
        ).locator("input")
        self.search_button: Locator = page.get_by_role("button", name="Search")
        self.add_employee_button: Locator = self.header_container.get_by_role(
            "button", name="Add"
        )
        self.employee_list_tab: Locator = page.get_by_role(
            "link", name=ExpectedMenuItems.EMPLOYEE_LIST
        )
        self.records_found: Locator = page.locator(".orangehrm-horizontal-padding span")
        self.pagination = self.page.get_by_role(
            "navigation", name="Pagination Navigation"
        )
        self.selected_page = self.pagination.locator(
            ".oxd-pagination-page-item--page-selected"
        )
        self.next_page_button = self.pagination.get_by_role("button").filter(
            has=self.page.locator(".bi-chevron-right")
        )

    def open(self) -> None:
        self.pim_menu.click()

    def click_add_employee_button(self) -> None:
        expect(self.add_employee_button).to_be_visible()
        expect(self.add_employee_button).to_be_enabled()
        self.add_employee_button.click()

    def create_employee(
        self,
        add_employee_page: AddEmployeePage,
    ) -> dict[str, str]:

        first_name = generate_first_name()
        middle_name = generate_middle_name()
        last_name = generate_last_name()
        employee_id = generate_employee_id()

        self.click_add_employee_button()
        add_employee_page.verify_add_employee_page()

        add_employee_page.add_employee(first_name, middle_name, last_name, employee_id)

        return {
            "first_name": first_name,
            "middle_name": middle_name,
            "last_name": last_name,
            "employee_id": employee_id,
        }

    def open_employee_list(self) -> None:
        self.pim_menu.click()
        self.employee_list_tab.click()

        expect(self.page).to_have_url(PIM_URL)

    def get_employee_name(self, employee: dict[str, str]) -> str:
        return f"{employee['first_name']} {employee['middle_name']}"

    def get_row_by_employee_id(self, employee_id: str) -> Locator:
        return self.employee_table.get_by_role("row").filter(
            has=self.page.get_by_role("cell", name=employee_id, exact=True)
        )

    def find_employee_row_by_id(self, employee_id: str) -> Locator:
        first_employee_row = self.employee_table.get_by_role("row").nth(1)
        expect(first_employee_row).to_be_visible()

        while True:
            current_page = self.selected_page.inner_text()
            employee_row = self.get_row_by_employee_id(employee_id)

            if employee_row.count() > 0:
                expect(employee_row).to_be_visible()
                return employee_row

            if self.next_page_button.count() == 0:
                break

            current_table_text = self.employee_table.inner_text()
            self.next_page_button.click()
            expect(self.selected_page).not_to_have_text(current_page)
            expect(self.employee_table).not_to_have_text(current_table_text)
            expect(first_employee_row).to_be_visible()

        raise AssertionError(
            f"Employee with ID '{employee_id}' was not found in the employee list"
        )

    def open_employee_for_edit(self, employee_id: str) -> None:
        self.open_employee_list()

        employee_row = self.find_employee_row_by_id(employee_id)

        edit_button = self._get_row_action_button(
            employee_row, self.EDIT_BUTTON_ICON_SELECTOR
        )
        expect(edit_button).to_be_visible()
        edit_button.click()

    def search_employee(
        self,
        employee_name: str | None = None,
        employee_id: str | None = None,
    ) -> None:
        if employee_name is not None:
            self.employee_name_input.fill(employee_name)

        if employee_id is not None:
            self.employee_id_input.fill(employee_id)

        self.search_button.click()

    def verify_employee_in_search_results(
        self, employee_id: str, employee_name: str, last_name: str
    ) -> None:
        expect(self.records_found).to_have_text(ExpectedMessages.SINGLE_RECORD_FOUND)

        employee_row = self.get_row_by_employee_id(employee_id)
        expect(employee_row).to_be_visible()

        expect(employee_row.get_by_role("cell").nth(1)).to_have_text(employee_id)
        expect(employee_row.get_by_role("cell").nth(2)).to_have_text(employee_name)
        expect(employee_row.get_by_role("cell").nth(3)).to_have_text(last_name)

    def delete_employee_by_id(self, employee_id: str) -> None:
        employee_row = self.get_row_by_employee_id(employee_id)

        expect(employee_row).to_be_visible()

        delete_button = self._get_row_action_button(
            employee_row, self.DELETE_BUTTON_ICON_SELECTOR
        )
        delete_button.click()

        self.page.get_by_role("button", name="Yes, Delete").click()

        expect(employee_row).to_have_count(0)

    def _get_row_action_button(
        self, employee_row: Locator, icon_selector: str
    ) -> Locator:
        return (
            employee_row.locator(".oxd-table-cell-actions")
            .get_by_role("button")
            .filter(has=self.page.locator(icon_selector))
        )

    def verify_employee_exists(self, employee_id: str) -> None:
        employee_row = self.get_row_by_employee_id(employee_id)

        expect(self.records_found).to_have_text(ExpectedMessages.SINGLE_RECORD_FOUND)
        expect(employee_row).to_be_visible()
