from data.config import Config

LOGIN_PATH = "/web/index.php/auth/login"
DASHBOARD_PATH = "/web/index.php/dashboard/index"
PIM_PATH = "/web/index.php/pim/viewEmployeeList"
ADD_EMPLOYEE_PATH = "/web/index.php/pim/addEmployee"
PIM_PERSONAL_DETAILS_PATH = "/web/index.php/pim/viewPersonalDetails"


LOGIN_URL = f"{Config.BASE_URL}{LOGIN_PATH}"
DASHBOARD_URL = f"{Config.BASE_URL}{DASHBOARD_PATH}"
PIM_URL = f"{Config.BASE_URL}{PIM_PATH}"
ADD_EMPLOYEE_URL = f"{Config.BASE_URL}{ADD_EMPLOYEE_PATH}"
PIM_PERSONAL_DETAILS_URL = f"{Config.BASE_URL}{PIM_PERSONAL_DETAILS_PATH}"

VALID_USERNAME = Config.ADMIN_USERNAME
VALID_PASSWORD = Config.ADMIN_PASSWORD

INVALID_USERNAME = "invalid_user"
INVALID_PASSWORD = "invalid_password"

EMPTY_FIELD = ""

QUICK_LAUNCH_BUTTON_NAMES = [
    "Assign Leave",
    "Leave List",
    "Timesheets",
    "Apply Leave",
    "My Leave",
    "My Timesheet",
]
