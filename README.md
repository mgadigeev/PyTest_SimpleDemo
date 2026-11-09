# PyTest_SimpleDemo

## Задача
Необходимо написать и протестировать функцию, которая рассчитывает итоговую цену товара после применения скидки. 
Требования:
- Скидка может быть в процентах, но не более 50%.
- Также есть минимальная цена — она не может быть меньше 1 рубля.

Функция реализована в модуле src/discount.py.
Тесты реализованы в модуле tests/test_discount.py

## Тестирование
### Как запустить
```bash
pip install pytest
pytest test_discount.py -v
```

### Ожидаемый результат
```
test_discount.py::test_no_discount PASSED
test_discount.py::test_regular_discount PASSED
test_discount.py::test_discount_capped_at_50_percent PASSED
test_discount.py::test_minimum_price PASSED

4 passed in 0.01s
```
