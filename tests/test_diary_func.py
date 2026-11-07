# test_diary_func.py
import pytest
from diary_func import (
    create_grade_book,
    add_student,
    add_grade,
    average,
    is_excellent,
    group_average,
)

# --- Фикстура: каждый тест получает свежий дневник ---
@pytest.fixture
def book():
    b = create_grade_book()
    add_student(b, "Аня")
    add_student(b, "Боря")
    return b

# --- Обычные тесты с assert ---
def test_add_student_creates_empty_list(book):
    assert "Аня" in book
    assert book["Аня"] == []

def test_average_with_grades(book):
    add_grade(book, "Аня", 5)
    add_grade(book, "Аня", 3)
    assert average(book, "Аня") == 4.0

def test_average_without_grades(book):
    # У Бори ещё нет оценок — средний балл 0
    assert average(book, "Боря") == 0.0

def test_is_excellent_true(book):
    add_grade(book, "Аня", 5)
    assert is_excellent(book, "Аня") is True

def test_is_excellent_false(book):
    # Нет оценок — не отличник
    assert is_excellent(book, "Боря") is False

# --- Параметризация: много сценариев в одном тесте ---
@pytest.mark.parametrize("grades, expected", [
    ([5, 5, 5], 5.0),
    ([2, 4], 3.0),
    ([3], 3.0),
    ([], 0.0),          # граничный случай: нет оценок
    ([2, 2, 2, 2], 2.0),
])
def test_average_parametrized(book, grades, expected):
    for g in grades:
        add_grade(book, "Аня", g)
    assert average(book, "Аня") == expected

# --- Проверка исключений ---
def test_add_grade_to_unknown_student_raises(book):
    with pytest.raises(KeyError):
        add_grade(book, "Вася", 5)

def test_grade_out_of_range_raises(book):
    with pytest.raises(ValueError):
        add_grade(book, "Аня", 6)

def test_duplicate_student_raises():
    book = create_grade_book()
    add_student(book, "Аня")
    with pytest.raises(ValueError, match="уже есть"):
        add_student(book, "Аня")
