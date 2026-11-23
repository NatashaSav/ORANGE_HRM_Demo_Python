from playwright.sync_api import expect

from data.constants import (
    DASHBOARD_URL,
    QUICK_LAUNCH_BUTTON_NAMES,
)
from data.expected_messages import ExpectedMessages
from pages.dashboard_page import DashboardPage


def test_dashboard_page_is_displayed(dashboard_page: DashboardPage):
    expect(dashboard_page.page).to_have_url(DASHBOARD_URL)
    expect(dashboard_page.dashboard_heading).to_be_visible()


def test_time_at_work_widget_content(dashboard_page: DashboardPage):
    expect(dashboard_page.time_at_work_widget).to_be_visible()
    expect(dashboard_page.get_attendance_status()).to_be_visible()
    expect(dashboard_page.get_attendance_details()).to_be_visible()
    expect(dashboard_page.get_attendance_button()).to_be_visible()
    expect(dashboard_page.get_attendance_chart()).to_be_visible()


def test_my_actions_widget_content(dashboard_page: DashboardPage):
    expect(dashboard_page.my_actions_widget).to_be_visible()

    my_action_items = dashboard_page.get_my_actions_items()
    expect(my_action_items.first).to_be_visible()

    for index in range(my_action_items.count()):
        item = my_action_items.nth(index)
        expect(dashboard_page.get_my_action_button(item)).to_be_visible()
        expect(dashboard_page.get_my_action_description(item)).not_to_be_empty()


def test_quick_launch_widget_content(dashboard_page: DashboardPage):
    expect(dashboard_page.quick_launch_widget).to_be_visible()

    quick_launch_items = dashboard_page.get_quick_launch_items()
    expect(quick_launch_items).to_have_count(len(QUICK_LAUNCH_BUTTON_NAMES))

    for index, expected_name in enumerate(QUICK_LAUNCH_BUTTON_NAMES):
        item = quick_launch_items.nth(index)

        expect(dashboard_page.get_quick_launch_button(item)).to_be_visible()
        expect(dashboard_page.get_quick_launch_button(item)).to_have_accessible_name(
            expected_name
        )
        expect(dashboard_page.get_quick_launch_label(item)).to_have_text(expected_name)


def test_buzz_latest_posts_widget_content(dashboard_page: DashboardPage):
    expect(dashboard_page.buzz_latest_post_widget).to_be_visible()

    cards = dashboard_page.get_buzz_widget_cards()
    expect(cards.first).to_be_visible()

    for index in range(cards.count()):
        card = cards.nth(index)

        expect(dashboard_page.get_buzz_card_header(card)).to_be_visible()
        expect(dashboard_page.get_buzz_author_name(card)).to_be_visible()
        expect(dashboard_page.get_buzz_publication_date(card)).to_be_visible()
        expect(dashboard_page.get_buzz_card_body(card)).to_be_visible()


def test_employees_on_leave_widget_content(dashboard_page: DashboardPage):
    widget = dashboard_page.employees_on_leave_widget
    expect(widget).to_be_visible()

    empty_state = dashboard_page.get_widget_empty_state(widget)
    employee_cards = dashboard_page.employee_leave_cards()

    expect(empty_state.or_(employee_cards.first).first).to_be_visible()

    if empty_state.is_visible():
        expect(empty_state).to_have_text(
            ExpectedMessages.EMPLOYEES_ON_LEAVE_EMPTY_STATE
        )
    else:

        for index in range(employee_cards.count()):
            card = employee_cards.nth(index)

            expect(dashboard_page.employee_leave_card_image(card)).to_be_visible()
            expect(dashboard_page.employee_leave_card_details(card)).to_be_visible()
            expect(dashboard_page.employee_leave_card_id(card)).to_be_visible()


def test_employee_distribution_by_sub_unit_widget_content(
    dashboard_page: DashboardPage,
):
    distribution_by_sub_unit = dashboard_page.employee_distribution_by_sub_unit_widget
    expect(distribution_by_sub_unit).to_be_visible()

    chart = dashboard_page.get_employee_distribution_chart(distribution_by_sub_unit)
    expect(chart).to_be_visible()

    chart_legend_items = dashboard_page.get_employee_distribution_chart_legend(
        distribution_by_sub_unit
    )
    expect(chart_legend_items).to_be_visible()


def test_employee_distribution_by_location_widget_content(
    dashboard_page: DashboardPage,
):
    distribution_by_location = dashboard_page.employee_distribution_by_location_widget
    expect(distribution_by_location).to_be_visible()

    chart = dashboard_page.get_employee_distribution_chart(distribution_by_location)
    expect(chart).to_be_visible()

    chart_legend_items = dashboard_page.get_employee_distribution_chart_legend(
        distribution_by_location
    )
    expect(chart_legend_items).to_be_visible()
