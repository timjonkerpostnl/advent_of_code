from typing import List

import pytest

from src.day6.assignment2 import process_file


def test_assignment2():
    assert process_file("input_test1.txt") == 71503
