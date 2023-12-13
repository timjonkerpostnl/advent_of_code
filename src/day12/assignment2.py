import re
from functools import cache
from typing import List

from tqdm import tqdm

from src.day12.assignment1 import replace_char_at_position


def sequence_correct(sequence: str, sequence_lengths: tuple[int, ...]):
    return known_sequences(sequence) == sequence_lengths


@cache
def sequence_potentially_correct(sequence: str, sequence_lengths: tuple[int, ...]):
    if not sequence_lengths:
        return False
    up_to_question = sequence.split("?", 1)[0]
    new_string = up_to_question.rstrip("#")
    num_trailing = len(up_to_question) - len(new_string)
    known_sequence = known_sequences(new_string)
    return (
        len(sequence_lengths) > len(known_sequence)
        and known_sequence == sequence_lengths[: (len(known_sequence))]
        and num_trailing <= sequence_lengths[len(known_sequence)]
    )


@cache
def known_sequences(input_str: str) -> tuple[int]:
    return tuple(len(match.group()) for match in re.finditer(r"#+", input_str))


@cache
def fill_in_character(sequence: str, sequence_lengths: tuple[int, ...]):
    up_to_question = sequence.split("?", 1)[0]
    last_dot_position = up_to_question.rfind(".")
    if last_dot_position >= 0:
        known_sequence = known_sequences(up_to_question[: last_dot_position + 1])
        sequence = sequence[last_dot_position:]
        sequence_lengths = sequence_lengths[len(known_sequence) :]

    unknown_position = sequence.find("?")

    found_valid = 0
    new_sequences = []
    found_damaged_sequences = known_sequences(sequence[:unknown_position])
    remaining_sequences = sequence_lengths[len(found_damaged_sequences) :]
    required_positions = sum(remaining_sequences) + len(remaining_sequences) - 1

    # match = re.search(r'[#?]\.+', sequence)
    # first_dot_index_after_damage = match.start() + 1
    # match = re.search(r'[?#]', sequence)
    # first_damage = match.start()
    if sequence_correct(sequence, sequence_lengths):
        # All damaged parts have been found rest should be . so one option from here
        found_valid += 1
    elif unknown_position > 0 and sequence[unknown_position - 1] == "#":
        # We are in a sequence
        if (
            found_damaged_sequences == sequence_lengths
            or sequence_lengths[len(found_damaged_sequences) - 1] == found_damaged_sequences[-1]
        ):
            # Last sequence is complete, should only place a . here
            new_sequence = replace_char_at_position(sequence, unknown_position, ".")
            new_sequences.append(new_sequence)
        else:
            # Last sequence is active, should only place a # here
            new_sequences.append(replace_char_at_position(sequence, unknown_position, "#"))
    elif unknown_position < len(sequence) - 1 and sequence[unknown_position + 1] == "#":
        # We are in a sequence
        match = re.search(r"#+", sequence)
        first_damaged_length = len(match.group())
        if first_damaged_length >= sequence_lengths[0]:
            new_sequences.append(replace_char_at_position(sequence, unknown_position, "."))
        else:
            new_sequences.append(replace_char_at_position(sequence, unknown_position, "."))
            new_sequences.append(replace_char_at_position(sequence, unknown_position, "#"))
    elif len(sequence) - unknown_position == required_positions:
        # There must be a # now because there is no room for slack left
        new_sequences.append(replace_char_at_position(sequence, unknown_position, "#"))
    # elif first_dot_index_after_damage - first_damage == sequence_lengths[0] and unknown_position <= first_dot_index_after_damage and '#' in sequence[first_damage:first_dot_index_after_damage]:
    #     # Everything in between these positions must be a #
    #     new_sequences.append(replace_char_at_position(sequence, unknown_position, "#"))
    else:
        new_sequences.append(replace_char_at_position(sequence, unknown_position, "."))
        new_sequences.append(replace_char_at_position(sequence, unknown_position, "#"))

    for new_sequence in new_sequences:
        remaining_unknown_positions = new_sequence.find("?") >= 0
        if remaining_unknown_positions and sequence_potentially_correct(new_sequence, sequence_lengths):
            found_valid += fill_in_character(new_sequence, sequence_lengths)
        elif not remaining_unknown_positions and sequence_correct(new_sequence, sequence_lengths):
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

            sequence += "."
            found_valid_sequences = fill_in_character(sequence, tuple(sequence_lengths))
            summed += found_valid_sequences

    return summed


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
