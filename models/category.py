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

    def add_product(self, product: Product) -> None:
        """Добавление нового продукта"""

        if isinstance(product, Product):
            self.__products.append(product)
            Category.category_count += 1

    @property
    def products(self) -> str:
        """геттер для списка продуктов"""

        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str
