from playwright.sync_api import Locator, Page


class DashboardPage:
    def __init__(self, page: Page) -> None:
        self.page: Page = page

        self.dashboard_heading: Locator = page.get_by_role("heading", name="Dashboard")
        self.widget_containers: Locator = page.locator(
            ".orangehrm-dashboard-widget.oxd-sheet"
        )
        self.time_at_work_widget: Locator = self.get_widget("Time at Work")
        self.my_actions_widget: Locator = self.get_widget("My Actions")
        self.quick_launch_widget: Locator = self.get_widget("Quick Launch")
        self.buzz_latest_post_widget: Locator = self.get_widget("Buzz Latest Posts")
        self.employees_on_leave_widget: Locator = self.get_widget(
            "Employees on Leave Today"
        )
        self.employee_distribution_by_sub_unit_widget: Locator = self.get_widget(
            "Employee Distribution by Sub Unit"
        )
        self.employee_distribution_by_location_widget: Locator = self.get_widget(
            "Employee Distribution by Location"
        )

    def get_widget(self, title: str) -> Locator:
        return self.widget_containers.filter(
            has=self.page.get_by_text(title, exact=True)
        )

    def get_attendance_status(self) -> Locator:
        return self.time_at_work_widget.locator(".orangehrm-attendance-card-state")

    def get_attendance_details(self) -> Locator:
        return self.time_at_work_widget.locator(".orangehrm-attendance-card-details")

    def get_attendance_button(self) -> Locator:
        return self.time_at_work_widget.locator(".orangehrm-attendance-card-action")

    def get_attendance_chart(self) -> Locator:
        return self.time_at_work_widget.locator(".emp-attendance-chart canvas")

    def get_widget_empty_state(self, widget: Locator) -> Locator:
        return widget.locator(".orangehrm-dashboard-widget-body-nocontent")

    def get_my_actions_items(self) -> Locator:
        return self.my_actions_widget.locator(".orangehrm-todo-list-item")

    def get_my_action_button(self, item: Locator) -> Locator:
        return item.get_by_role("button")

    def get_my_action_description(self, item: Locator) -> Locator:
        return item.locator("p")

    def get_quick_launch_items(self) -> Locator:
        return self.quick_launch_widget.locator(".orangehrm-quick-launch-card")

    def get_quick_launch_button(self, item: Locator) -> Locator:
        return item.locator("button")

    def get_quick_launch_label(self, item: Locator) -> Locator:
        return item.locator("p")

    def get_buzz_widget_cards(self) -> Locator:
        return self.buzz_latest_post_widget.locator(".orangehrm-buzz-widget-card")

    def get_buzz_card_header(self, card: Locator) -> Locator:
        return card.locator(".orangehrm-buzz-widget-header")

    def get_buzz_card_body(self, card: Locator) -> Locator:
        return card.locator(".orangehrm-buzz-widget-body")

    def get_buzz_author_name(self, card: Locator) -> Locator:
        return card.locator(".orangehrm-buzz-widget-header-emp")

    def get_buzz_publication_date(self, card: Locator) -> Locator:
        return card.locator(".orangehrm-buzz-widget-header-time")

    def employee_leave_cards(self) -> Locator:
        return self.employees_on_leave_widget.locator(".orangehrm-leave-card")

    def employee_leave_card_image(self, card: Locator) -> Locator:
        return card.locator(".orangehrm-leave-card-profile-image")

    def employee_leave_card_details(self, card: Locator) -> Locator:
        return card.locator(".orangehrm-leave-card-details")

    def employee_leave_card_id(self, card: Locator) -> Locator:
        return card.locator(".orangehrm-leave-card-emp-id")

    def get_employee_distribution_chart(self, widget: Locator) -> Locator:
        return widget.locator(".oxd-pie-chart")

    def get_employee_distribution_chart_legend(self, widget: Locator) -> Locator:
        return widget.locator(".oxd-chart-legend")
