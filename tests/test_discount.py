import pytest
from discount import apply_discount


def test_no_discount():
    # Без скидки цена не меняется
    assert apply_discount(100, 0) == 100.0


def test_regular_discount():
    # Скидка 20% от 100 = 80
    assert apply_discount(100, 20) == 80.0


def test_discount_capped_at_50_percent():
    # Скидка 70% обрезается до 50%, итог = 50
    assert apply_discount(100, 70) == 50.0


def test_minimum_price():
    # Скидка 50% от 1.5 = 0.75, но минимум — 1.0
    assert apply_discount(1.5, 50) == 1.0
