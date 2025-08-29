from models.product import Product

class Category:
    """ Класс для представления категории продуктов """

    # Атрибуты класса
    category_count: int = 0  # количество категорий
    product_count: int = 0   # количество товаров

    name: str                # имя категории
    description: str         # описание категории продуктов
    products: list[Product]  # список продуктов в данной категории

    def __init__(self, name: str, description: str, products: list[Product]):
        """ Инициализация экземпляра класса """

        self.name = name
        self.description = description
        self.products = products.copy()
        Category.category_count += 1
        Category.product_count = len(self.products)
