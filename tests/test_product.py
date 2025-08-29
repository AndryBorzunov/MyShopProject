import pytest

from models.product import Product


@pytest.fixture
def product_sony():
    return Product("Sony ZX", "Смартфон", 10500, 10)


def test_init(product_sony):
    assert product_sony.name == "Sony ZX"
    assert product_sony.description == "Смартфон"
    assert product_sony.price == 10500
    assert product_sony.quantity == 10
