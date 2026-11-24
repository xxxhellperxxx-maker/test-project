"""Каталог товаров: цена в рублях и необязательная скидка в процентах."""

PRODUCTS = {
    "book": {"title": "Книга", "price": 500},
    "pen": {"title": "Ручка", "price": 50, "discount": 10},
    "bag": {"title": "Рюкзак", "price": 2500, "discount": 20},
}


def get_product(sku):
    if sku not in PRODUCTS:
        raise ValueError(f"Unknown product: {sku}")
    return PRODUCTS[sku]
