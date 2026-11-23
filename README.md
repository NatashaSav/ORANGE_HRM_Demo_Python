# OrangeHRM UI Tests

A learning project for automating the [OrangeHRM Open Source Demo](https://opensource-demo.orangehrmlive.com/) with Python, Playwright, and Pytest.

> This is a public demo site with shared test data. Do not use real passwords or personal information in this project.

## Test Coverage

- **Login:** valid credentials, invalid credentials, and required fields.
- **Dashboard:** widget content, My Actions, Quick Launch, Buzz posts, attendance, employee distribution, and empty states.
- **PIM:** employee list, adding, editing, searching by employee ID or name, and deleting employees.

## Project Structure

```text
.
├── data/          # Test configuration and expected test data
├── pages/         # Page Objects and reusable UI components  
├── tests/         # Automated test scenarios and fixtures
├── utils/         # Test data generation and helper functions
├── .env.example
├── requirements.txt
└── README.md
```

Page Objects encapsulate page-specific locators and actions. The reusable `EmployeeForm` component provides shared employee name and ID field locators to the add-employee and personal-details pages. Shared fixtures in `tests/conftest.py` authenticate the browser and manage test employees.

## Requirements

- Python 3.12.
- Chromium installed for Playwright.

Package versions are pinned in `requirements.txt`.

## Installation

From the project root, create and activate a virtual environment, then install the dependencies and browser:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m playwright install chromium
```

In VS Code, select the Python interpreter from `.venv` using **Python: Select Interpreter**.

On Windows, activate the environment with `.venv\Scripts\activate`, then run the package and browser installation commands above.

## Environment Variables

Create a local `.env` file in the project root using `.env.example` as a template:

```env
BASE_URL=https://opensource-demo.orangehrmlive.com
ADMIN_USERNAME=your_username
ADMIN_PASSWORD=your_password
```

`data/config.py` loads these values from the project-root `.env` file and raises an error if a required value is missing. The `.env` file is ignored by Git; do not commit credentials.

Invalid credentials used by negative login tests are test inputs, not environment secrets. They are defined in `data/constants.py`.

## Running Tests

Run the full test suite from the project root with `.venv` activated:

```bash
python -m pytest
```

Run a specific test module:

```bash
python -m pytest tests/test_pim.py
```

Run a single test:

```bash
python -m pytest tests/test_dashboard.py::test_quick_launch_widget_content
```

Run tests with the browser visible:

```bash
python -m pytest --headed tests/test_login.py
```

The VS Code **Run and Debug** configuration can also launch the selected Dashboard test. Ensure the project root is open as the workspace and `.env` is configured before debugging.
