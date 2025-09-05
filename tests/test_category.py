import pytest

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
    assert category_smartphone.products == "Sony ZX, 10500 руб. Остаток: 10 шт.\n"
    assert category_smartphone.category_count == 1
    assert category_smartphone.product_count == 1


@pytest.fixture
def product_add():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 18000.0, 5)


def test_add_product(category_smartphone, product_add):
    category_smartphone.add_product(product_add)
    assert category_smartphone.product_count == 2
    assert (
        category_smartphone.products
        == "Sony ZX, 10500 руб. Остаток: 10 шт.\nSamsung Galaxy S23 Ultra, 18000.0 руб. Остаток: 5 шт.\n"
    )


@pytest.fixture
def str_result():
    return "Смартфоны, количество продуктов: 10 шт."


def test_str(category_smartphone, str_result):
    assert str(category_smartphone) == str_result


def test_add_product_error(category_smartphone):
    with pytest.raises(TypeError, match="Попытка добавить объект другого типа"):
        category_smartphone.add_product("not product")


@pytest.fixture
def category_full(product_sony, product_add):
    return Category("Смартфоны", "Смартфоны как средство коммуникации", [product_sony, product_add])


def test_middle_price(category_full):
    assert category_full.middle_price() == 14250.0


@pytest.fixture
def category_empty():
    return Category("Смартфоны", "Смартфоны как средство коммуникации", [])


def test_middle_price_empty(category_empty):
    assert category_empty.middle_price() == 0
