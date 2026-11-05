"""Unit-тесты для модуля services.

Поддерживают запуск как через `pytest`, так и через стандартный `python -m unittest`.
"""

import unittest
from src.models import BaseTaskItem
from src.services import process_raw_data


class TestServices(unittest.TestCase):
    """Набор тестов для бизнес-логики."""

    def test_process_raw_data_success(self) -> None:
        """Проверка успешной обработки и фильтрации активных записей."""
        raw_input: list[dict[str, object]] = [
            {"id": "A1", "name": "Тестовый прибор", "value": "100.5", "is_active": True},
            {"id": "A2", "name": "Неактивный прибор", "value": 200.0, "is_active": False},
        ]

        result = process_raw_data(raw_input)

        self.assertTrue(result.success)
        self.assertEqual(result.total_count, 1)
        self.assertEqual(len(result.processed_items), 1)

        item = result.processed_items[0]
        self.assertIsInstance(item, BaseTaskItem)
        self.assertEqual(item.id, "A1")
        self.assertEqual(item.value, 100.5)

    def test_process_raw_data_skips_invalid(self) -> None:
        """Проверка пропуска некорректных записей без падения скрипта."""
        bad_input: list[dict[str, object]] = [
            {"id": "BAD-1", "name": "", "value": -50.0},  # Отрицательное значение и пустое имя
        ]

        result = process_raw_data(bad_input)

        self.assertTrue(result.success)
        self.assertEqual(result.total_count, 0)
        self.assertEqual(len(result.processed_items), 0)


if __name__ == "__main__":
    unittest.main()
