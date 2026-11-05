"""Модуль бизнес-логики и обработки данных."""

import logging
from src.models import BaseTaskItem, TaskResult

logger = logging.getLogger(__name__)


def process_raw_data(raw_items: list[dict[str, object]]) -> TaskResult:
    """Очищает, валидирует и обрабатывает список сырых словарей.

    :param raw_items: Неструктурированные данные (например, из JSON, CSV или Excel).
    :return: Валидированный результат TaskResult.
    """
    valid_items: list[BaseTaskItem] = []

    for idx, raw in enumerate(raw_items, start=1):
        try:
            # Pydantic автоматически валидирует и приводит типы
            item = BaseTaskItem.model_validate(raw)
            if item.is_active:
                valid_items.append(item)
        except Exception as e:
            logger.warning("Пропущена некорректная запись #%d: %s (Ошибка: %s)", idx, raw, e)

    return TaskResult(
        total_count=len(valid_items),
        processed_items=valid_items,
        success=True,
    )
