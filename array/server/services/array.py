from numbers import Number
from typing import Any


def clean_and_get_sum(array: list[Any]) -> tuple[int, list[Number]]:
    """Создает новый массив без строк и считает сумму во время фильтрации массива."""
    s = 0
    new_array = []
    for item in array:
        if isinstance(item, Number):
            s += item
            new_array.append(item)

    return s, new_array


def clean_array_avg(array: list[Any]) -> list[Number]:
    """
    Чистит массив от строк, сортирует по возрастанию и добавляет в
    конец среднее арифметическое чисел массива.
    """
    s, array = clean_and_get_sum(array)
    if not array:
        return []

    array.sort()
    array.append(s/len(array))
    return array
