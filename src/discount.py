def apply_discount(price: float, discount_percent: float) -> float:
    """
    Возвращает цену после скидки.
    - price: исходная цена (должна быть > 0)
    - discount_percent: процент скидки (0..50, всё что больше — обрезается до 50)
    Итоговая цена не может быть меньше 1.0.
    """
    if price <= 0:
        raise ValueError("Цена должна быть положительной")

    if discount_percent < 0:
        raise ValueError("Скидка не может быть отрицательной")

    if discount_percent > 50:
        discount_percent = 50

    final_price = price * (1 - discount_percent / 100)

    if final_price < 1.0:
        return 1.0

    return round(final_price, 2)
