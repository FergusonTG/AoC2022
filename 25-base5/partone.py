"""Solve the puzzle by adding up all the numbers."""

import sys

import base5

if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()

    total = 0
    for line in lines:
        total += base5.base5_to_int(line)

    print("Total =", base5.int_to_base5(total))
