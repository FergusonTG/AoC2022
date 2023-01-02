

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


if __name__ == "__main__":
    # start python with one cmd line argument
    # e.g. python partone.cmd 2000000 < input
    BASELINE_Y = int(sys.argv[1], 10)


    lines = sys.stdin.read().splitlines()
    pairs = [get_scanner_beacon(line) for line in lines]
    baseline = set()
    beacons_in_baseline = set()

    for (scanner, beacon) in pairs:
        # print(scanner, beacon, manhattan(scanner, beacon))
        horizontal = manhattan(scanner, beacon) - abs(BASELINE_Y - y_of(scanner))
        if horizontal < 0:
            continue

        for x in range(x_of(scanner) - horizontal, x_of(scanner) + horizontal + 1):
            baseline.add(x)

        if y_of(beacon) == BASELINE_Y:
            print("To remove:", x_of(beacon))
            beacons_in_baseline.add(x_of(beacon))

    # remove beacons that are in the row
    print(f"Set of beacons in baseline: {beacons_in_baseline}")
    baseline  -= beacons_in_baseline

    # print(f"     {sorted(baseline)}")
    print(f"Excluded: {len(baseline)}")
