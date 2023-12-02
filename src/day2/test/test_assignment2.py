from src.day2.assignment2 import process_games


def test_process_games():
    assert process_games("test_input2.txt") == 2286
