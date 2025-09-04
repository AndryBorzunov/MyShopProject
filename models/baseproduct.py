from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseProduct(ABC):
    """Абстрактный класс для реализации продуктов"""

    @classmethod
    @abstractmethod
    def new_product(cls, dict_product: Dict[str, Any]) -> Any | None:
        """Метод для преобразования словаря с данными о продукте в экземпляр класса Product"""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Переопределение строкового представления класса"""
        pass

    @abstractmethod
    def __add__(self, other: Any) -> float | Any:
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float) -> None:
        """Сеттер для аттрибута price"""
        pass
