"""
config.py — Reads all settings from the .env file.

Why: Keeping secrets (DB password, JWT key) out of source code is a
basic security requirement. python-dotenv loads the .env file, and
pydantic-settings validates each value at startup so the app fails
fast if something is missing.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Application
    app_env: str = "development"
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    frontend_origin: str = "http://localhost:8000"

    # Database
    db_host: str = "localhost"
    db_port: int = 3306
    db_name: str = "retail_forecast_db"
    db_user: str = "root"
    db_password: str = ""

    # Inventory / ML
    service_level_z: float = 1.65
    ordering_cost_s: float = 100.0
    holding_rate: float = 0.20

    # Security (Phase 7)
    secret_key: str = "change-me"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    # Tell pydantic-settings where to find the .env file
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",        # silently ignore unknown keys in .env
    )


# Single shared instance — import this everywhere
settings = Settings()
