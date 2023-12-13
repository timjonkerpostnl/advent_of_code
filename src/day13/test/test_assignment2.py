from typing import List

import numpy as np
import pytest

from src.day13.assignment2 import (
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
            None,
        ),
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
            None,
        ),
    ],
)
def test_find_vertical_reflection(input, expected):
    assert find_vertical_reflection(input) == expected


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
            3,
        ),
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
            1,
        ),
    ],
)
def test_find_horizontal_reflection(input, expected):
    assert find_horizontal_reflection(input) == expected


def test_assignment2():
    assert process_file("input_test1.txt") == 400
