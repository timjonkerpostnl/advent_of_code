from typing import List

import pytest

from src.day12.assignment1 import process_file


def test_assignment1():
    assert process_file("input_test1.txt") == 4361
