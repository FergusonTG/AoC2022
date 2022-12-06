"""Part two: common members of three strings."""


import string


LETTERS = string.ascii_lowercase + string.ascii_uppercase
INPUT_FILE = "input"


def priority(letter):
    """Convert a letter to a priority."""
    return 1 + LETTERS.index(letter)


def common_letter(inpt0, inpt1, inpt2):
    """Find letter common to three inputs."""
    ret = [letter for letter in inpt0 if letter in inpt1 and letter in inpt2]
    return ret[0]


if __name__ == "__main__":
    total = 0
    with open(INPUT_FILE, "r") as inputs:
        while True:
            try:
                letter = common_letter(next(inputs), next(inputs), next(inputs))
                total += priority(letter)
            except StopIteration:
                break

    print(f"Total: {total}")
