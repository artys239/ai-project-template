"""Конфигурация проекта и чтение переменных окружения."""

import os
from pathlib import Path

try:
    from pydantic_settings import BaseSettings, SettingsConfigDict

    class AppSettings(BaseSettings):
        """Настройки проекта через pydantic-settings."""

        app_name: str = "MyAutomationTask"
        app_env: str = "development"
        log_level: str = "INFO"

        base_dir: Path = Path(__file__).resolve().parent.parent

        model_config = SettingsConfigDict(
            env_file=".env",
            env_file_encoding="utf-8",
            extra="ignore",
        )

except ImportError:
    from pydantic import BaseModel

    class AppSettings(BaseModel):  # type: ignore[no-redef]
        """Резервный класс настроек без pydantic-settings."""

        app_name: str = os.getenv("APP_NAME", "MyAutomationTask")
        app_env: str = os.getenv("APP_ENV", "development")
        log_level: str = os.getenv("LOG_LEVEL", "INFO")

        base_dir: Path = Path(__file__).resolve().parent.parent


# Глобальный объект настроек
settings = AppSettings()
