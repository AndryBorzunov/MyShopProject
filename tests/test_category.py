import  pytest
from models.category import Category
from models.product import Product


@pytest.fixture
def product_sony():
    return Product("Sony ZX", "Смартфон", 10500, 10)


@pytest.fixture
def category_smartphone(product_sony):
    return Category("Смартфоны", "Смартфоны как средство коммуникации", [product_sony])


def test_init(category_smartphone, product_sony):
    assert category_smartphone.name == "Смартфоны"
    assert category_smartphone.description == "Смартфоны как средство коммуникации"
    assert category_smartphone.products == [product_sony]
    assert category_smartphone.category_count == 1
    assert category_smartphone.product_count == 1
