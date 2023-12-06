from typing import List

import pytest

from src.day7.assignment1 import process_file, calculate_distance, ways_to_beat_record

def test_assignment1():
    assert process_file("input_test1.txt") == 288
