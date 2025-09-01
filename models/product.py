from  typing import Type

class Product:
    """ Класс для представления продукта """

    name: str         # Наименование продукта
    description: str  # Описание продукта
    __price: float      # Стоимость
    quantity: int     # Количество

    def __init__(self, name, description, price, quantity):
        """ Метод для инициализации экземпляра класса """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    @property
    def price(self):
        return self.__price


    @price.setter
    def price(self, value: float):
        if value > 0:
            self.__price = value
        else:
            print("Цена не должна быть нулевая или отрицательная")


    @classmethod
    def new_product(cls, dict_product: dict[str, str | float | int]):
        return cls(dict_product["name"], dict_product["description"], dict_product["price"], dict_product["quantity"])
