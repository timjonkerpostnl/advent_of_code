from typing import List

import pytest

from src.day12.assignment2 import process_file


def test_assignment2():
    assert process_file("input_test1.txt") == 467835
