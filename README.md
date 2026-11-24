# Тестовый проект магазина (с ошибкой)

Небольшой проект на Python для проверки агента AI Bug Investigator — [xxxhellperxxx-maker/Automated-Bug-Investigator-PR-Reviewer](https://github.com/xxxhellperxxx-maker/Automated-Bug-Investigator-PR-Reviewer). В коде намеренно оставлена ошибка — её агент должен найти, воспроизвести тестами и исправить.

## Состав

* `shop/catalog.py` — каталог товаров: цена и необязательная скидка;
* `shop/pricing.py` — цена единицы товара со скидкой и стоимость доставки;
* `shop/orders.py` — сумма заказа;
* `tests/test_orders.py` — 7 тестов (pytest).

## Известная ошибка

Заказ с товаром без скидки (например, `book`) падает с `KeyError: 'discount'`: функция `unit_price` в `shop/pricing.py` читает поле `discount` напрямую, а у части товаров его нет. Ошибка всплывает в `shop/orders.py`, а причина — в `shop/pricing.py`.

На исходном коде падают 2 теста из 7:

```bash
pip install -r requirements.txt && python -m pytest -q
```

## Как проверить агента

Запустите агента по инструкции из его репозитория и в форме укажите:

* **Репозиторий:** свой форк этого проекта, например `ваш-логин/test-project` (режим GitHub; агенту нужно право записи, чтобы создать ветку и PR) — или склонируйте проект в `local-projects/test-project` агента и укажите `local:test-project` (локальный режим, GitHub не нужен);
* **Текст ошибки** — стек-трейс или просто описание:

```text
Traceback (most recent call last):
  File "/srv/shop/shop/orders.py", line 15, in order_total
    subtotal = order_subtotal(lines)
  File "/srv/shop/shop/orders.py", line 10, in order_subtotal
    total += unit_price(line["sku"]) * line["qty"]
  File "/srv/shop/shop/pricing.py", line 7, in unit_price
    discount = product["discount"]
KeyError: 'discount'
```

Ожидаемый результат: агент воспроизводит 2 падения, указывает причину в `shop/pricing.py`, исправляет (`product.get("discount", 0)`) и подтверждает исправление — проходят все 7 тестов.

## Непрерывная интеграция (необязательно)

GitHub Actions — второй, независимый контур проверки для агента. Чтобы его включить, создайте в репозитории файл `.github/workflows/tests.yml` (через сайт GitHub: **Add file → Create new file**; для загрузки через git токену нужно право `workflow`):

```yaml
name: tests
on:
  push:
  pull_request:
jobs:
  pytest:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: python -m pytest -q
```
