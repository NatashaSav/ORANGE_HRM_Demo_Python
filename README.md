# OrangeHRM UI Tests

A learning project for automating the [OrangeHRM Open Source Demo](https://opensource-demo.orangehrmlive.com/) with Python, Playwright, and Pytest. The current tests cover the login page.

> This is a public demo site with shared test data. Do not use real passwords or personal information in this project.

## Current Test Coverage

- Successful login: verifies that the Dashboard opens and its `Dashboard` heading is visible.
- Unsuccessful login: verifies the `Invalid credentials` message for the input combinations defined with `pytest.mark.parametrize`.

The successful-login credentials are loaded from `.env` by `data/config.py`. Login URLs and test input values are defined in `data/constants.py`; expected UI messages are defined in `data/expected_messages.py`.

## Project Structure

```text
.
├── data/
│   ├── config.py          # Loads and validates environment variables
│   ├── constants.py       # URLs and test input values
│   └── expected_messages.py  # Expected messages displayed by the UI
├── pages/
│   └── login_page.py      # Login page object
├── tests/
│   ├── conftest.py        # Shared test fixtures
│   └── test_login.py      # Successful and unsuccessful login tests
├── test-data/             # Directory for test data files
├── .gitignore             # Excludes local and generated files
├── .env.example           # Example environment variable names
├── requirements.txt       # Pinned Python dependencies
└── README.md
```

`LoginPage` encapsulates the login page locators and actions. The tests describe user flows and assertions, using the `page` fixture provided by `pytest-playwright` and the shared `login_page` fixture from `tests/conftest.py`.

## Requirements

- Python 3.12 (the project dependencies were verified with this version).
- The Chromium browser installed for Playwright.

Package versions are pinned in `requirements.txt` to make the environment reproducible and avoid unexpected changes when Pytest or Playwright is updated.

## Installation

From the project root, run:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m playwright install chromium
```

After activating the virtual environment, `(.venv)` should appear in your terminal prompt. In VS Code, select the Python interpreter from this environment using **Python: Select Interpreter**.

On Windows, activate the environment with `.venv\Scripts\activate`, then run the package and browser installation commands above.

## Environment Variables

Create a local `.env` file in the project root using `.env.example` as a template, then set the demo site's base URL and login credentials:

```env
BASE_URL=https://opensource-demo.orangehrmlive.com
ADMIN_USERNAME=your_username
ADMIN_PASSWORD=your_password
```

`data/config.py` loads these values from the project-root `.env` file, regardless of the directory from which you run the tests. The `.env` file is ignored by Git; do not commit credentials.

The credentials are read from `.env` as `ADMIN_USERNAME` and `ADMIN_PASSWORD`. Invalid credentials used by negative login tests are test inputs, not environment secrets, and are defined in `data/constants.py`.

## Running Tests

From the project root with `.venv` activated, run the full test suite:

```bash
python -m pytest
```

Run the login tests only:

```bash
python -m pytest tests/test_login.py
```

Use quiet output:

```bash
python -m pytest -q tests/test_login.py
```

Run the browser in headed mode for debugging:

```bash
python -m pytest --headed tests/test_login.py
```

`python -m pytest` runs Pytest using the selected Python interpreter. The `-q` (`quiet`) option shortens the output without changing which checks are performed.
