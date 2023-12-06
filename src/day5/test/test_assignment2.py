from typing import List

import pytest

from src.day5.alternative import problem2
from src.day5.assignment2 import process_file


def test_assignment2():
    assert process_file("input_test1.txt") == 46


def test_assignment2_alternative():
    assert problem2("input_test1.txt") == 46
