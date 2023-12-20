from typing import List

import numpy as np
import pytest

from src.day20.assignment1 import process_file

@pytest.mark.parametrize("file, expected", [
    ("input_test1.txt", 32000000),
    ("input_test2.txt", 11687500),
])
def test_assignment1(file, expected):
    assert process_file(file) == expected
