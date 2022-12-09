"""Check the forest for visible trees."""

import sys
from pprint import pprint


def check_sight_line(rows):
    """Check each tree for visibility."""
    cols = [* zip(* rows)]
    ret = [[0 for _ in cols] for _ in rows]

    for y, row in enumerate(rows):
        for x, tree in enumerate(row):
            if (x == 0 or x == len(cols) - 1 or y == 0 or y == len(rows) - 1):
                # leave it at default zero
                continue
            ret[y][x] = 1
            # look left, right, up, down
            for view in (row[x::-1], row[x:], cols[x][y::-1], cols[x][y:]):
                # print(view, end = " ")
                ret[y][x] *= count_trees(view)


            # print(f"ret[{y}][{x}] = {ret[y][x]}")
        # print()
    return ret


def count_trees(line):
    for ret, tree in enumerate(line):
        if ret == 0:
            continue
        if tree >= line[0]:
            return ret
    return len(line) - 1


if __name__ == "__main__":
    inpt = [line.strip() for line in sys.stdin]

    grid = check_sight_line(inpt)

    best_score = max(max(row) for row in grid)
    print(best_score)
