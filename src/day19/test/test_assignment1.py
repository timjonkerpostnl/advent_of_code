from typing import List

import numpy as np
import pytest

from src.day19.assignment1 import process_file


def test_assignment1():
    assert process_file("input_test1.txt") == 19114
