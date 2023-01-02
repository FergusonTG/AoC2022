"""Solve Advent of Code 2022: day 18."""

import sys

from obsipy import is_touching


def main():
    """Check for number of free faces on rocks."""
    lines = sys.stdin.read().splitlines()
    rocks = [
        (int(a), int(b), int(c)) for (a, b, c) in (line.split(",") for line in lines)
    ]

    count = 0
    for num, rock1 in enumerate(rocks):
        for rock2 in rocks[num + 1 :]:
            if is_touching(rock1, rock2):
                count += 1

    print(len(rocks) * 6 - count * 2)


if __name__ == "__main__":
    main()
