from data.config import Config

LOGIN_PATH = "/web/index.php/auth/login"
DASHBOARD_PATH = "/web/index.php/dashboard/index"

LOGIN_URL = f"{Config.BASE_URL}{LOGIN_PATH}"
DASHBOARD_URL = f"{Config.BASE_URL}{DASHBOARD_PATH}"

VALID_USERNAME = Config.ADMIN_USERNAME
VALID_PASSWORD = Config.ADMIN_PASSWORD

INVALID_USERNAME = "invalid_user"
INVALID_PASSWORD = "invalid_password"

EMPTY_FIELD = ""
