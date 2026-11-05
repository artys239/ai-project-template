"""Главная точка входа приложения."""

import logging
import sys
from src.config import settings
from src.services import process_raw_data

# Базовая настройка логирования
logging.basicConfig(
    level=getattr(logging, settings.log_level.upper(), logging.INFO),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("main")


def main() -> int:
    """Основной сценарий выполнения задачи."""
    logger.info("Запуск приложения: %s (Окружение: %s)", settings.app_name, settings.app_env)

    # Пример входных сырых данных для демонстрации пайплайна
    sample_data: list[dict[str, object]] = [
        {"id": "DEV-01", "name": "Датчик давления", "value": "1250.50", "is_active": True},
        {"id": "DEV-02", "name": "Клапан регулирующий", "value": 4500, "is_active": True},
        {"id": "DEV-03", "name": "Устаревший датчик", "value": 0, "is_active": False},
    ]

    try:
        result = process_raw_data(sample_data)
        logger.info("Обработка завершена успешно. Валидных записей: %d", result.total_count)
        for item in result.processed_items:
            logger.info("-> %s | %s | %s", item.id, item.name, item.value)
        return 0
    except Exception as exc:
        logger.critical("Критический сбой выполнения пайплайна: %s", exc, exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
