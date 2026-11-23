import pytest
from playwright.sync_api import expect

from data.constants import PIM_URL
from pages.add_employee_page import AddEmployeePage
from pages.personal_details_page import PersonalDetailsPage
from pages.pim_page import PIMPage
from utils.data_generator import generate_first_name


def test_pim_page_is_displayed(pim_page: PIMPage):
    expect(pim_page.page).to_have_url(PIM_URL)
    expect(pim_page.pim_heading).to_be_visible()


def test_add_employee(
    pim_page: PIMPage,
    add_employee_page: AddEmployeePage,
    personal_details_page: PersonalDetailsPage,
    employee_cleanup,
):
    employee = pim_page.create_employee(add_employee_page)
    employee_cleanup(employee)

    personal_details_page.verify_personal_details_page()
    personal_details_page.verify_employee_details(
        employee["first_name"],
        employee["middle_name"],
        employee["last_name"],
        employee["employee_id"],
    )


def test_edit_employee(
    created_employee: dict[str, str],
    pim_page: PIMPage,
    personal_details_page: PersonalDetailsPage,
):
    new_first_name = generate_first_name()
    pim_page.open_employee_for_edit(created_employee["employee_id"])

    personal_details_page.verify_personal_details_page()
    personal_details_page.verify_employee_details(
        created_employee["first_name"],
        created_employee["middle_name"],
        created_employee["last_name"],
        created_employee["employee_id"],
    )

    personal_details_page.edit_first_name(new_first_name)
    personal_details_page.click_save_button()
    personal_details_page.verify_first_name(new_first_name)


@pytest.mark.parametrize(
    "search_by",
    ["employee_id", "employee_name"],
    ids=["by_employee_id", "by_employee_name"],
)
def test_search_employee(
    created_employee: dict[str, str], pim_page: PIMPage, search_by: str
):
    employee_name = pim_page.get_employee_name(created_employee)
    pim_page.open_employee_list()

    if search_by == "employee_id":
        pim_page.search_employee(employee_id=created_employee["employee_id"])
    else:
        pim_page.search_employee(employee_name=employee_name)

    pim_page.verify_employee_in_search_results(
        created_employee["employee_id"], employee_name, created_employee["last_name"]
    )


def test_delete_employee(
    pim_page: PIMPage,
    add_employee_page: AddEmployeePage,
    employee_cleanup,
):
    employee = pim_page.create_employee(add_employee_page)
    employee_cleanup(employee)

    pim_page.open_employee_list()
    pim_page.search_employee(employee_id=employee["employee_id"])

    pim_page.verify_employee_exists(employee["employee_id"])
    pim_page.delete_employee_by_id(employee["employee_id"])
