import pytest

from models.smartphone import Smartphone


@pytest.fixture
def smartphone_new():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


def test_init(smartphone_new):
    assert smartphone_new.name == "Iphone 15"
    assert smartphone_new.description == "512GB, Gray space"
    assert smartphone_new.price == 210000.0
    assert smartphone_new.quantity == 8
    assert smartphone_new.efficiency == 98.2
    assert smartphone_new.model == "15"
    assert smartphone_new.memory == 512
    assert smartphone_new.color == "Gray space"
