"""Check the forest for visible trees."""

import sys
from pprint import pprint


def check_visibility(rows):
    """Check each tree for visibility."""
    cols = [* zip(* rows)]
    ret = [[False for _ in cols] for _ in rows]

    for y, row in enumerate(rows):
        for x, tree in enumerate(row):
            ret[y][x] = (
                x == 0 or x == len(cols) - 1
                or y == 0 or y == len(rows) - 1
                or tree > max(row[:x])
                or tree > max(row[x+1:])
                or tree > max(cols[x][:y])
                or tree > max(cols[x][y+1:])
            )
            # print(f"ret[{y}][{x}] = {ret[y][x]}")
        # print()
    return ret



if __name__ == "__main__":
    inpt = [line.strip() for line in sys.stdin]

    grid = check_visibility(inpt)

    visible_count = sum(sum(row) for row in grid)
    print(visible_count)
