# diary_func.py

MIN_GRADE = 2
MAX_GRADE = 5

def create_grade_book():
    """Создаёт пустой дневник (словарь)."""
    return {}

def add_student(book, name):
    """Добавляет студента. Имя должно быть уникальным."""
    if name in book:
        raise ValueError(f"Студент {name!r} уже есть в дневнике")
    book[name] = []

def add_grade(book, name, grade):
    """Ставит студенту оценку. Оценка — целое число от 2 до 5."""
    if name not in book:
        raise KeyError(f"Студента {name!r} нет в дневнике")
    if not isinstance(grade, int):
        raise TypeError("Оценка должна быть целым числом")
    if not MIN_GRADE <= grade <= MAX_GRADE:
        raise ValueError(f"Оценка должна быть от {MIN_GRADE} до {MAX_GRADE}")
    book[name].append(grade)

def average(book, name):
    """Средний балл студента. Если оценок нет — 0.0."""
    grades = book.get(name, [])
    if not grades:
        return 0.0
    return sum(grades) / len(grades)

def is_excellent(book, name):
    """Отличник — тот, у кого все оценки пятёрки и их хотя бы одна."""
    grades = book.get(name, [])
    return bool(grades) and all(g == 5 for g in grades)

def group_average(book):
    """Средний балл по всем студентам группы."""
    all_grades = [g for grades in book.values() for g in grades]
    if not all_grades:
        return 0.0
    return sum(all_grades) / len(all_grades)
