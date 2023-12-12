from typing import List

import pytest

from src.day11.assignment2 import process_file


@pytest.mark.parametrize("distance, expected", [(2, 374), (10, 1030), (100, 8410)])
def test_assignment2(distance, expected):
    assert process_file("input_test1.txt", distance) == expected
