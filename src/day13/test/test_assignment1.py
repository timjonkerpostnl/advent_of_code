from typing import List

import numpy as np
import pytest

from src.day13.assignment1 import (
    process_file,
    find_vertical_reflection,
    find_horizontal_reflection,
)


@pytest.mark.parametrize(
    "input, expected",
    [
        (
            np.array(
                [
                    [1, 0, 1, 1, 0, 0, 1, 1, 0],
                    [0, 0, 1, 0, 1, 1, 0, 1, 0],
                    [1, 1, 0, 0, 0, 0, 0, 0, 1],
                    [1, 1, 0, 0, 0, 0, 0, 0, 1],
                    [0, 0, 1, 0, 1, 1, 0, 1, 0],
                    [0, 0, 1, 1, 0, 0, 1, 1, 0],
                    [1, 0, 1, 0, 1, 1, 0, 1, 0],
                ]
            ),
            5,
        ),
    ],
)
def test_find_vertical_reflection(input, expected):
    assert find_vertical_reflection(input) == 5


@pytest.mark.parametrize(
    "input, expected",
    [
        (
            np.array(
                [
                    [1, 0, 0, 0, 1, 1, 0, 0, 1],
                    [1, 0, 0, 0, 0, 1, 0, 0, 1],
                    [0, 0, 1, 1, 0, 0, 1, 1, 1],
                    [1, 1, 1, 1, 1, 0, 1, 1, 0],
                    [1, 1, 1, 1, 1, 0, 1, 1, 0],
                    [0, 0, 1, 1, 0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 1, 0, 0, 1],
                ]
            ),
            5,
        ),
    ],
)
def test_find_horizontal_reflection(input, expected):
    assert find_horizontal_reflection(input) == 4


def test_assignment1():
    assert process_file("input_test1.txt") == 405
