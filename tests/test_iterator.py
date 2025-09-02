import pytest

from models.category import Category
from models.product import Product
from models.iterator import Iterator


@pytest.fixture
def product_sony():
    return Product("Sony ZX", "Смартфон", 10500, 10)


@pytest.fixture
def category_smartphone(product_sony):
    return Category("Смартфоны", "Смартфоны как средство коммуникации", [product_sony])

@pytest.fixture
def str_result():
    return "Sony ZX, 10500 руб. Остаток: 10 шт."


def test_iterator(category_smartphone, str_result):
    category_iterator = Iterator(category_smartphone)
    for item in category_iterator:
        assert item == str_result
