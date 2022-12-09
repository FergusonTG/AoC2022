"""Check the forest for visible trees."""

import sys
from pprint import pprint


def check_visibility(lines):
    """Check rows and columns and merge them."""
    grid1 = check_rows(lines)
    grid2 = check_cols(lines)

    for row in range(len(lines)):
        for col in range(len(lines[0])):
            grid1[row][col] = grid1[col][row] or grid2[col][row]
    return grid1


def check_rows(lines):
    """Read the lines and make a grid of visible trees."""
    grid = [ [] for _ in lines ]
    for rownum, row in enumerate(lines):
        grid[rownum] = check_line(row)

    return grid


def check_cols(lines):
    """Read the columns and make a grid of visible trees."""
    grid = [ [] for _ in lines[0] ]
    for colnum in range(len(lines[0])):
        col = [line[colnum] for line in lines]
        grid[colnum] = check_line(col)
    return [*zip(*grid)]


def check_line(row):
    """Return a row with True for visible trees."""
    ret = [False for _ in row]
    tallest_so_far = " "

    for source in (enumerate(row), reversed(list(enumerate(row)))):
        tallest_so_far = " "
        for treenum, tree in source:
            if tree > tallest_so_far:
                tallest_so_far = tree
                ret[treenum] = True

    return ret


if __name__ == "__main__":
    inpt = [line.strip() for line in sys.stdin]

    grid = check_visibility(inpt)

    visible_count = sum(sum(row) for row in grid)
    print(visible_count)
