from playwright.sync_api import Page


class EmployeeForm:
    def __init__(self, page: Page) -> None:
        self.first_name_input = page.get_by_placeholder("First Name")
        self.middle_name_input = page.get_by_placeholder("Middle Name")
        self.last_name_input = page.get_by_placeholder("Last Name")
        self.employee_id_input = (
            page.locator(".oxd-input-group")
            .filter(has=page.get_by_text("Employee Id", exact=True))
            .locator("input")
        )
