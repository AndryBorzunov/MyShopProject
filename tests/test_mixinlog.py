from models.product import Product
from models.smartphone import Smartphone


def test_mixin_log(capsys):
    Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Xiaomi Redmi Note 11, 1024GB, Синий, 31000.0, 14)"

    Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 86.7, "Redmi Note 11", 1024, "синий")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Xiaomi Redmi Note 11, 1024GB, Синий, 31000.0, 14)"
