from typing import List

import pytest

from src.day9.assignment1 import process_file, get_difference_sequence, extrapolate


@pytest.mark.parametrize(
    "numbers, expected",
    [([0, 3, 6, 9, 12, 15], [3, 3, 3, 3, 3]), ([1, 3, 6, 10, 15, 21], [2, 3, 4, 5, 6])],
)
def test_get_difference_sequence(numbers, expected):
    assert get_difference_sequence(numbers) == expected


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([[0, 3, 6, 9, 12, 15], [3, 3, 3, 3, 3], [0, 0, 0, 0]], 18),
        ([[1, 3, 6, 10, 15, 21], [2, 3, 4, 5, 6], [1, 1, 1, 1], [0, 0, 0]], 28),
    ],
)
def test_extrapolate(numbers, expected):
    assert extrapolate(numbers) == expected


def test_assignment1():
    assert process_file("input_test1.txt") == 114
