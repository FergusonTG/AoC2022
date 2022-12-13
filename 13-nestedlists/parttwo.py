

import sys
from functools import cmp_to_key


def compare(one, two):
    """Compare two lists element by element."""
    setup = ((2 if (type(one).__name__ == 'list') else 0)
             + (1 if (type(two).__name__ == 'list') else 0)
             )
    # print(f"Comparing {one} and {two}: {setup=}")

    if setup == 0:  # int & int
        return -1 if one < two else 0 if one == two else 1
    if setup == 1:  # int & list
        return compare([one], two)
    if setup == 2:  # list & int
        return compare(one, [two])

    for a, b in zip(one, two):
        cmp = compare(a, b)
        if cmp != 0:
            return cmp
    # print(f"Bottom of function: {one=}, {two=}")
    return 1 if len(one) > len(two) else 0 if len(one) == len(two) else -1


if __name__ == "__main__":
    separators = ['[[2]]', '[[6]]']
    text = sys.stdin.read()
    lines = [eval(s) for s in text.splitlines() + separators if s]
    lines.sort(key=cmp_to_key(compare))
    one = 1 + lines.index(eval(separators[0]))
    two = 1 + lines.index(eval(separators[1]))

    print(f"{one=}, {two=}, product={one * two}")
