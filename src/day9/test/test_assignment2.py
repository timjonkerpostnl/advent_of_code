from typing import List

import pytest

from src.day9.assignment2 import process_file, extrapolate_backward


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([[0, 3, 6, 9, 12, 15], [3, 3, 3, 3, 3], [0, 0, 0, 0]], -3),
        ([[1, 3, 6, 10, 15, 21], [2, 3, 4, 5, 6], [1, 1, 1, 1], [0, 0, 0]], 0),
    ],
)
def test_extrapolate_backward(numbers, expected):
    assert extrapolate_backward(numbers) == expected


def test_assignment2():
    assert process_file("input_test1.txt") == 2
