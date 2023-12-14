from typing import List

import numpy as np
import pytest

from src.day14.assignment1 import process_file, weight_in_column


@pytest.mark.parametrize(
    "row, expected",
    [
        ("OO.O.O..##", 34),
        ("...OO....O", 27),
    ],
)
def test_weight_in_column(row: str, expected: int):
    row = list(row)
    assert weight_in_column(row) == expected


def test_assignment1():
    assert process_file("input_test1.txt") == 136
