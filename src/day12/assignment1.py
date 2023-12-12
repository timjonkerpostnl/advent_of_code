import re
from typing import List

from tqdm import tqdm


def sequence_correct(sequence, sequence_lengths):
    return [len(match.group()) for match in re.finditer(r"#+", sequence)] == sequence_lengths


def replace_char_at_position(input_string, position, new_char):
    string_list = list(input_string)
    string_list[position] = new_char
    result_string = "".join(string_list)

    return result_string


def sequence_potentially_correct(sequence, sequence_lengths):
    up_to_question = sequence.split("?", 1)[0]
    new_string = up_to_question.rstrip("#")
    known_sequence = [len(match.group()) for match in re.finditer(r"#+", new_string)]
    return known_sequence == sequence_lengths[: (len(known_sequence))]


def fill_in_character(unknown_positions, sequence, sequence_lengths, found_valid):
    up = unknown_positions.pop(0)
    new_sequence_a = replace_char_at_position(sequence, up, ".")
    new_sequence_b = replace_char_at_position(sequence, up, "#")
    if unknown_positions and sequence_potentially_correct(new_sequence_a, sequence_lengths):
        found_valid = fill_in_character(unknown_positions.copy(), new_sequence_a, sequence_lengths, found_valid)
    elif not unknown_positions and sequence_correct(new_sequence_a, sequence_lengths):
        found_valid += 1
    if unknown_positions and sequence_potentially_correct(new_sequence_b, sequence_lengths):
        found_valid = fill_in_character(unknown_positions.copy(), new_sequence_b, sequence_lengths, found_valid)
    elif not unknown_positions and sequence_correct(new_sequence_b, sequence_lengths):
        found_valid += 1

    return found_valid


def process_file(file_name: str) -> int:
    summed = 0
    with open(file_name) as f:
        for idx, line in tqdm(enumerate(f)):
            stripped_line = line.strip()
            sequence, sequence_lengths = stripped_line.split(" ")
            sequence_lengths = [int(x) for x in sequence_lengths.split(",")]
            unknown_positions = [i for i, char in enumerate(sequence) if char == "?"]

            found_valid_sequences = fill_in_character(unknown_positions, sequence, sequence_lengths, 0)
            summed += found_valid_sequences

    return summed


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
