"""Tests for Product class"""

import pytest
from python_advanced.unittesting.to_test import Product


@pytest.fixture(name="default_product")
def fixture_default_product():
    """Create product without quantity"""
    return Product("Carrot", 12.5)


@pytest.fixture(name="product")
def fixture_product():
    """Create product with quantity"""
    return Product("Carrot", 12.5, 5)


def test_default_quantity(default_product):
    """Check default quantity"""
    assert default_product.quantity == 1


def test_setting_attributes(product):
    """Check all attributes if we create product with quantity"""
    assert product.quantity == 5 and product.title == "Carrot" and product.price == 12.5


def test_subtract_quantity_default(product):
    """
    Check how change product quantity if we call
    subtract_quantity without transmitting parameter
    """
    product.subtract_quantity()
    assert product.quantity == 4


def test_subtract_quantity(product):
    """
    Check how change product quantity if we call
    subtract_quantity with transmitting parameter
    """
    product.subtract_quantity(2)
    assert product.quantity == 3


@pytest.mark.parametrize("elems, exception", [("f", TypeError),
                                              (([2, 5], [9, 9]), TypeError),
                                              (10, ValueError)])
def test_subtract_quantity_errors(product, elems, exception):
    """
    Check:
    ValueError - for the possibility of a negative number of products;
    TypeError - for the possibility of transmission argument with incorrect type.
    """
    with pytest.raises(exception):
        product.subtract_quantity(elems)


def test_add_quantity_default(product):
    """Check how change product quantity if we call add_quantity without transmitting parameter"""
    product.add_quantity()
    assert product.quantity == 6


def test_add_quantity(product):
    """Check how change product quantity if we call add_quantity with transmitting parameter"""
    product.add_quantity(2)
    assert product.quantity == 7


@pytest.mark.parametrize("elem, error", [("few", TypeError),
                                         (([2, 5], [9, 9]), TypeError)])
def test_add_quantity_type_error(product, elem, error):
    """
    Check the occurrence TypeError - for checking the possibility
    of transmission argument with incorrect type
    """
    with pytest.raises(error):
        product.add_quantity(elem)


def test_change_price(product):
    """Check the correctness of changing price"""
    product.change_price(90.5)
    assert product.price == 90.5


def test_change_price_value_error(product):
    """
    Check the occurrence of ValueError - for checking
    the possibility of a negative price
    """
    with pytest.raises(ValueError):
        product.change_price(-10.8)
