"""Модели данных и схемы валидации (Pydantic v2)."""

from pydantic import BaseModel, Field


class BaseTaskItem(BaseModel):
    """Пример базовой модели элемента данных.

    Замените поля под требования конкретной задачи.
    """

    id: str = Field(description="Уникальный идентификатор записи")
    name: str = Field(min_length=1, description="Наименование объекта/оборудования")
    value: float = Field(ge=0.0, description="Числовое значение (цена, мощность, расход и т.д.)")
    is_active: bool = Field(default=True, description="Флаг активности")


class TaskResult(BaseModel):
    """Итоговый результат обработки пайплайна."""

    total_count: int = Field(ge=0)
    processed_items: list[BaseTaskItem] = Field(default_factory=list)
    success: bool = True
