from typing import List

import numpy as np
import pytest

from src.day19.assignment2 import (
    process_file
)

def test_assignment1():
    range1 = range(0, 999999, 2)
    range2 = range(1, 999999, 3)
    assert min(set(range1).intersection(range2)) == 4
