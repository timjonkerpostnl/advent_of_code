import re


def find_first_and_last_digit(input_string: str):
    first_digit_match = re.search(r"\d", input_string)
    last_digit_match = re.search(r"\d", input_string[::-1])

    first_digit = first_digit_match.group() if first_digit_match else None
    last_digit = last_digit_match.group() if last_digit_match else None

    return first_digit, last_digit


summed = 0
with open("input.txt") as f:
    for idx, line in enumerate(f):
        # if idx > 10:
        #     break
        stripped_line = line.strip()
        first_digit, last_digt = find_first_and_last_digit(stripped_line)
        number = first_digit + last_digt
        # print(f"String {stripped_line} produced {number}")
        summed += int(number)
