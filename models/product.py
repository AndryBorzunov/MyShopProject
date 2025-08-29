

class Product:
    """ Класс для представления продукта """

    name: str         # Наименование продукта
    description: str  # Описание продукта
    price: float      # Стоимость
    quantity: int     # Количество

    def __init__(self, name, description, price, quantity):
        """ Метод для инициализации экземпляра класса """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
