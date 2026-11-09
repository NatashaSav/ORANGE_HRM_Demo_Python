import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / ".env")


def _required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(
            f"Environment variable {name} is missing or empty. "
            "Set it in the project .env file."
        )
    return value


class Config:
    BASE_URL = _required_env("BASE_URL").rstrip("/")

    ADMIN_USERNAME = _required_env("ADMIN_USERNAME")
    ADMIN_PASSWORD = _required_env("ADMIN_PASSWORD")
