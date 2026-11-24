from shop.pricing import delivery_cost, unit_price


def order_subtotal(lines):
    """Сумма заказа без доставки. lines — список {"sku": ..., "qty": ...}."""
    total = 0
    for line in lines:
        if line["qty"] <= 0:
            raise ValueError("Quantity must be positive")
        total += unit_price(line["sku"]) * line["qty"]
    return round(total, 2)


def order_total(lines):
    subtotal = order_subtotal(lines)
    return round(subtotal + delivery_cost(subtotal), 2)
