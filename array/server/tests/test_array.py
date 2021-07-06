from services.array import clean_array_avg


def test_empty_array():
    assert clean_array_avg([]) == []


def test_avg():
    assert clean_array_avg([1, 2, 3]) == [1, 2, 3, 2]
    assert clean_array_avg([3.6, 3.7, 3.8, 3.9]) == [3.6, 3.7, 3.8, 3.9, 3.7500000000000004]


def test_clean():
    assert clean_array_avg([-1, 'trash', 0, 'dump', 1, ['array']]) == [-1, 0, 1, 0]


def test_sort():
    assert clean_array_avg([0, 5, -10, 15, 3.5]) == [-10, 0, 3.5, 5, 15, 2.7]


def test_only_strings():
    assert clean_array_avg(['asdas', 'ss']) == []
