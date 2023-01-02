

import sys
import re
from pprint import pprint
from operator import itemgetter


def get_scanner_beacon(string):
    bits = string.split(": ")
    patt = re.compile(r"x=(-?\d+), y=(-?\d+)")
    scanner = tuple(int(b, 10) for b in patt.search(bits[0]).groups())
    beacon = tuple(int(b, 10) for b in patt.search(bits[1]).groups())
    return (scanner, beacon)


def manhattan(one, two):
    return abs(one[0] - two[0]) + abs(one[1] - two[1])


x_of = itemgetter(0)
y_of = itemgetter(1)


def get_exclusions(pairs, baseline_y):
    baseline = set()

    for (scanner, beacon) in pairs:
        horizontal = manhattan(scanner, beacon) - abs(baseline_y - y_of(scanner))
        if horizontal < 0:
            continue

        for x in range(x_of(scanner) - horizontal, x_of(scanner) + horizontal + 1):
            baseline.add(x)

    return baseline


def sign(number):
    return -1 if number < 0 else 0 if number == 0 else 1


if __name__ == "__main__":
    # start python with one cmd line argument
    # e.g. python parttwo.cmd 4000000 < input

    raise NotImplementedError("Have not finished this puzzle.")

    MAX_COORDINATE = int(sys.argv[1], 10)
    lines = sys.stdin.read().splitlines()

    pairs = [get_scanner_beacon(line) for line in lines]
    scanners = [pair[0] for pair in pairs]

    man_dist = {scanner: manhattan(beacon, scanner)
             for scanner, beacon in pairs
             }

    for num, scanner1 in enumerate(scanners):
        for scanner2 in scanners[num + 1:]:
            if manhattan(scanner1, scanner2) == man_dist[scanner1] + man_dist[scanner2] + 2:
                x_dir = sign(x_of(scanner1) - x_of(scanner2))
                y_dir = sign(y_of(scanner1) - y_of(scanner2))
                diagonal = x_dir * y_dir

                print({0:"/",1:"\\"}[diagonal], scanner1, scanner2)
                if (x_dir, y_dir) == (1, 1):
                    points1 = [(x_of(scanner1) + man_dist[scanner1] - i, y_of(scanner1) - i)
                               for i in range(man_dist[scanner1])]

