"""Advent of Code 2022: packing haversacks."""


import string


LETTERS = string.ascii_lowercase + string.ascii_uppercase
INPUT_FILE = "input"


def common_letter(input):
    """Find a common letter between the two halves."""
    half = len(input) // 2
    ret = [letter for letter in input[:half] if letter in input[half:]]
    return ret[0]


def priority(letter):
    """Convert a letter to a priority."""
    return 1 + LETTERS.index(letter)


if __name__ == "__main__":
    with open(INPUT_FILE, "r") as inputs:
        total = sum(
            priority(letter) for letter in [common_letter(inpt) for inpt in inputs]
        )
    print(f"Total: {total}")
