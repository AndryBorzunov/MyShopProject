from typing import Any, Dict


class Product:
    """Класс для представления продукта"""

    name: str  # Наименование продукта
    description: str  # Описание продукта
    __price: float  # Стоимость
    quantity: int  # Количество

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод для инициализации экземпляра класса"""

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для аттрибута price"""

        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для аттрибута price"""

        if value > 0:
            self.__price = value
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, dict_product: Dict[str, Any]) -> Any | None:
        """Метод для преобразования словаря с данными о продукте в экземпляр класса Product"""

        if (
            "name" in dict_product
            and "description" in dict_product
            and "price" in dict_product
            and "quantity" in dict_product
        ):
            return cls(
                dict_product["name"], dict_product["description"], dict_product["price"], dict_product["quantity"]
            )
        else:
            return None

    def __str__(self) -> str:
        """Переопределение строкового представления класса"""

        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> float:
        """Сложение общей суммы стоимости продуктов при сложении экземпляров класса"""

        if isinstance(other, Product):
            return self.__price * self.quantity + other.price * other.quantity
        else:
            return self.__price * self.quantity
