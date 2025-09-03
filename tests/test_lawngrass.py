import pytest

from models.lawngrass import LawnGrass


@pytest.fixture
def lawngrass_new():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


def test_init(lawngrass_new):
    assert lawngrass_new.name == "Газонная трава"
    assert lawngrass_new.description == "Элитная трава для газона"
    assert lawngrass_new.price == 500.0
    assert lawngrass_new.quantity == 20
    assert lawngrass_new.country == "Россия"
    assert lawngrass_new.germination_period == "7 дней"
    assert lawngrass_new.color == "Зеленый"
