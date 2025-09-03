from typing import Any

from models.product import Product


class Category:
    """Класс для представления категории продуктов"""

    # Атрибуты класса
    category_count: int = 0  # количество категорий
    product_count: int = 0  # количество товаров

    name: str  # имя категории
    description: str  # описание категории продуктов
    __products: list[Product]  # список продуктов в данной категории

    def __init__(self, name: str, description: str, products: list[Product]):
        """Инициализация экземпляра класса"""

        self.name = name
        self.description = description
        self.__products = products.copy()
        Category.category_count += 1
        Category.product_count = len(self.__products)

    def add_product(self, product: Any) -> None:
        """Добавление нового продукта"""

        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Попытка добавить объект другого типа")

    @property
    def products(self) -> str:
        """геттер для списка продуктов (строковое представление)"""

        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    @property
    def products_list(self) -> list[Product]:
        """геттер для списка продуктов (список объектов)"""

        return self.__products

    def __str__(self) -> str:
        """
        Переопределение строкового представления класса -
        выводит имя категории и общее количество продуктов
        """

        summa = 0
        for item in self.__products:
            summa += item.quantity
        return f"{self.name}, количество продуктов: {summa} шт."
