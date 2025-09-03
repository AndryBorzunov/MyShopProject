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


def test_price(product_sony):
    assert product_sony.price == 10500


@pytest.fixture
def new_price():
    return 10100


def test_price_set(product_sony, new_price):
    product_sony.price = new_price
    assert product_sony.price == new_price


@pytest.mark.parametrize(
    "data_in, data_output",
    [
        (
            {
                "name": "Samsung Galaxy S23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5,
            },
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        )
    ],
)
def test_new_product(data_in, data_output):
    new_product = Product.new_product(data_in)
    assert new_product.name == data_output.name
    assert new_product.description == data_output.description
    assert new_product.price == data_output.price
    assert new_product.quantity == data_output.quantity


@pytest.mark.parametrize(
    "data_in, data_output",
    [
        (
            {
                "name": "Samsung Galaxy S23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
            },
            None,
        ),
    ],
)
def test_bad_data(data_in, data_output):
    new_product = Product.new_product(data_in)
    assert new_product is None


@pytest.fixture
def str_result():
    return "Sony ZX, 10500 руб. Остаток: 10 шт."


def test_str(product_sony, str_result):
    assert str(product_sony) == str_result


@pytest.fixture
def product_other():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 18000.0, 5)


def test_add(product_sony, product_other):
    assert product_sony + product_other == 195000


def test_add_error(product_sony):
    with pytest.raises(TypeError, match="Попытка сложения объектов разных типов"):
        product_sony + "not product"
