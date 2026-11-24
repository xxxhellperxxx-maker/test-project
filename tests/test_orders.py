import pytest

from shop.orders import order_subtotal, order_total
from shop.pricing import delivery_cost, unit_price


def test_unit_price_with_discount():
    assert unit_price("pen") == 45


def test_unit_price_without_discount():
    assert unit_price("book") == 500


def test_order_total_with_delivery():
    assert order_total([{"sku": "pen", "qty": 2}]) == 390


def test_order_with_product_without_discount():
    assert order_subtotal([{"sku": "book", "qty": 2}, {"sku": "pen", "qty": 1}]) == 1045


def test_free_delivery_from_3000():
    assert delivery_cost(3000) == 0
    assert delivery_cost(2999) == 300


def test_unknown_product():
    with pytest.raises(ValueError):
        unit_price("phone")


def test_quantity_must_be_positive():
    with pytest.raises(ValueError):
        order_subtotal([{"sku": "pen", "qty": 0}])
