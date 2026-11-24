from shop.catalog import get_product


def unit_price(sku):
    """Цена одной единицы товара с учётом скидки."""
    product = get_product(sku)
    discount = product.get("discount", 0)
    return round(product["price"] * (100 - discount) / 100, 2)


def delivery_cost(subtotal):
    """Доставка бесплатна для заказов от 3000 рублей."""
    return 0 if subtotal >= 3000 else 300
