from typing import List

import numpy as np
import pytest

from src.day17.assignment2 import (
    process_file
)

@pytest.mark.parametrize("file, expected", [
    ("input_test1.txt", 94),
    ("input_test2.txt", 71),
])
def test_assignment1(file, expected):
    assert process_file(file) == expected
