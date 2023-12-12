import re
from functools import cache
from typing import List

from tqdm import tqdm

from src.day12.assignment1 import replace_char_at_position


def sequence_correct(sequence: str, sequence_lengths: tuple[int, ...]):
    return tuple(len(match.group()) for match in re.finditer(r"#+", sequence)) == sequence_lengths


def sequence_potentially_correct(sequence: str, sequence_lengths: tuple[int, ...]):
    if not sequence_lengths:
        return False
    up_to_question = sequence.split("?", 1)[0]
    new_string = up_to_question.rstrip("#")
    num_trailing = len(up_to_question) - len(new_string)
    known_sequence = tuple(len(match.group()) for match in re.finditer(r"#+", new_string))
    return (
        len(sequence_lengths) > len(known_sequence)
        and known_sequence == sequence_lengths[: (len(known_sequence))]
        and num_trailing <= sequence_lengths[len(known_sequence)]
    )


@cache
def fill_in_character(sequence: str, sequence_lengths: tuple[int, ...]):
    unknown_positions = [i for i, char in enumerate(sequence) if char == "?"]
    up = unknown_positions.pop(0)

    found_valid = 0
    new_sequences = []
    found_damaged_sequences = [len(match.group()) for match in re.finditer(r"#+", sequence[:up])]
    # remaining_sequences = sequence_lengths[len(found_damaged_sequences):]
    # required_positions = sum(remaining_sequences) + len(remaining_sequences) - 1
    if sequence_correct(sequence, sequence_lengths):
        # All damaged parts have been found rest should be . so one option from here
        found_valid += 1
    elif up > 0 and sequence[up - 1] == "#":
        # We are in a sequence
        if (
            found_damaged_sequences == sequence_lengths
            or sequence_lengths[len(found_damaged_sequences) - 1] == found_damaged_sequences[-1]
        ):
            # Last sequence is complete, should only place a . here
            new_sequence = replace_char_at_position(sequence, up, ".")
            new_sequence1 = new_sequence[up + 1 :]
            new_sequences.append(new_sequence1)
            up_to_question = sequence.split("?", 1)[0]
            known_sequence = [len(match.group()) for match in re.finditer(r"#+", up_to_question)]
            sequence_lengths = sequence_lengths[len(known_sequence) :]
        else:
            # Last sequence is active, should only place a # here
            new_sequences.append(replace_char_at_position(sequence, up, "#"))
    # elif up < len(sequence) - 1 and sequence[up + 1] == "#":
    # We are in a sequence
    # elif len(sequence) - up == required_positions:
    #     # There must be a # now because there is no room for slack left
    #     new_sequences.append(replace_char_at_position(sequence, up, "#"))
    else:
        new_sequences.append(replace_char_at_position(sequence, up, "."))
        new_sequences.append(replace_char_at_position(sequence, up, "#"))

    for new_sequence in new_sequences:
        if unknown_positions and sequence_potentially_correct(new_sequence, sequence_lengths):
            found_valid += fill_in_character(new_sequence, sequence_lengths)
        elif not unknown_positions and sequence_correct(new_sequence, sequence_lengths):
            found_valid += 1

    return found_valid


def process_file(file_name: str) -> int:
    summed = 0
    with open(file_name) as f:
        for idx, line in tqdm(enumerate(f)):
            stripped_line = line.strip()
            sequence, sequence_lengths = stripped_line.split(" ")
            sequence = "?".join([sequence] * 5)
            sequence_lengths = ",".join([sequence_lengths] * 5)
            sequence_lengths = [int(x) for x in sequence_lengths.split(",")]

            found_valid_sequences = fill_in_character(sequence, tuple(sequence_lengths))
            summed += found_valid_sequences

    return summed


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
