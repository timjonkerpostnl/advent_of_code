from typing import List

import pytest

from src.day10.assignment2_speedup import process_file


@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("input_test1.txt", 1),
        ("input_test21.txt", 4),
        ("input_test22.txt", 4),
        ("input_test23.txt", 8),
        ("input_test24.txt", 10),
    ],
)
def test_assignment2(file_name, expected):
    assert process_file(file_name, True) == expected
