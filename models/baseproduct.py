from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseProduct(ABC):
    """Абстрактный класс для реализации продуктов"""

    @classmethod
    @abstractmethod  # pragma: no cover
    def new_product(cls, dict_product: Dict[str, Any]) -> Any | None:
        """Метод для преобразования словаря с данными о продукте в экземпляр класса Product"""
        pass

    @abstractmethod  # pragma: no cover
    def __str__(self) -> str:
        """Переопределение строкового представления класса"""
        pass

    @abstractmethod  # pragma: no cover
    def __add__(self, other: Any) -> float | Any:
        """Сложение общей суммы стоимости продуктов при сложении экземпляров класса"""
        pass

    @property
    @abstractmethod  # pragma: no cover
    def price(self) -> float:
        """Геттер для аттрибута price"""
        pass

    @price.setter
    @abstractmethod  # pragma: no cover
    def price(self, value: float) -> None:
        """Сеттер для аттрибута price"""
        pass
