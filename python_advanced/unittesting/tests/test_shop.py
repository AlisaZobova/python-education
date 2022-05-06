"""Tests for Shop class"""

import pytest
from python_advanced.unittesting.to_test import Shop, Product


@pytest.fixture(name="default_shop")
def fixture_default_shop():
    """Create shop without arguments"""
    return Shop()


@pytest.fixture(name="shop")
def fixture_shop():
    """Create shop with arguments"""
    return Shop([Product("Carrot", 12.5, 5), Product("Oil", 12.5, 5)])


def test_default_products(default_shop):
    """Check default products"""
    assert default_shop.products == []


def test_setting_attributes(shop):
    """Check amount of products if we create object with attributes"""
    assert len(shop.products) == 2


def test_add_product(shop):
    """Check the increase of the list length when add a new product"""
    shop.add_product(Product("Olive", 15.5))
    assert len(shop.products) == 3


def test_det_product_index_good(shop):
    """Check returned index existing product"""
    assert shop._get_product_index("Carrot") == 0


def test_det_product_index_bad(shop):
    """Check returned index if we transmit non-existing product"""
    assert shop._get_product_index("Car") is None


def test_sell_product_return(shop):
    """Check returned value"""
    assert shop.sell_product("Carrot", 1) == 12.5


def test_sell_product_norm(shop):
    """Check result if product quantity is more than requested"""
    shop.sell_product("Carrot", 1)
    assert shop.money == 12.5 and len(shop.products) == 2 and shop.products[0].quantity == 4


def test_sell_product_more(shop):
    """Check result if product quantity is smaller than requested"""
    with pytest.raises(ValueError):
        shop.sell_product("Carrot", 6)


def test_sell_product_eq(shop):
    """Check result if product quantity is the same as requested"""
    shop.sell_product("Carrot", 5)
    assert shop.money == 62.5 and len(shop.products) == 1
