"""Work out the monkeys yelling."""

import sys
from pprint import pprint
import operator

OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,
}


def is_int(object):
    return isinstance(object, int)


def read_input(lines):
    """Read the lines and make a dict."""
    return {monkeyname: int(value) if value.isnumeric() else value.split()
            for monkeyname, value in [line.partition(": ")[0::2] for line in lines]
            }


if __name__ == "__main__":
    inpt = sys.stdin.read().splitlines()
    base = read_input(inpt)

    while not isinstance(base['root'], int):
        for monkey, shout in base.items():
            if is_int(shout):
                continue
            if is_int(base[shout[0]]) and is_int(base[shout[2]]):
                base[monkey] = OPERATORS[shout[1]](base[shout[0]], base[shout[2]])
                print(monkey, shout, base[monkey])

    print(base['root'])
