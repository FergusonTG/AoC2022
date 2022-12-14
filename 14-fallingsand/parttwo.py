"""Solve day 14 of AoC: falling grains of sand."""

import sys
from operator import itemgetter
import time


def drop(grid, size):
    """drop a grain of sand."""
    bottom = size[3] + 1

    x, y = 500, 0
    if grid[(x, y)] == 'o':
        raise IndexError("No more room for sand, please")

    falling = True
    while falling:
        if y == bottom:
            falling = False
        elif (x, y + 1) not in grid:
            x, y = x, y + 1
        elif (x - 1, y + 1) not in grid:
            x, y = x - 1, y + 1
        elif (x + 1, y + 1) not in grid:
            x, y = x + 1, y + 1
        else:
            falling = False

    grid[(x, y)] = 'o'


def read_grid(input_text):
    """Get the input string and parse it into a grid."""
    lines = input_text.splitlines()

    grid = {(500, 0): '+'}

    for line in lines:
        coords = [str_to_tuple(s) for s in line.split(' -> ')
                  ]
        for idx in range(1, len(coords)):
            for coord in path(coords[idx - 1], coords[idx]):
                grid[coord] = "#"

    return grid


def path(start, finish):
    """return list of tuples filling in the whole path."""
    if start[0] == finish[0]:  # vertical
        beg, fin = sorted([start[1], finish[1]])
        return [(finish[0], y) for y in range(beg, fin + 1)]

    if start[1] == finish[1]:  # horizontal
        beg, fin = sorted([start[0], finish[0]])
        return [(x, finish[1]) for x in range(beg, fin + 1)]

    raise ValueError("Path must be vertical or horizontal.")


def str_to_tuple(string):
    """break a comma-separated coordinate pair into a tuple."""
    x, _, y = string.partition(',')
    return (int(x, 10), int(y, 10))


def size_of(grid):
    """Find max and min x and y values."""
    points = grid.keys()
    xes = set(point[0] for point in points)
    yes = set(point[1] for point in points)
    return (min(xes), min(yes), max(xes), max(yes))


def grid_to_text(grid):
    """Display the grid on the terminal."""
    size = size_of(grid)
    text_array = [["." for _ in range(size[2] - size[0] + 1)]
                  for _ in range(size[3] - size[1] + 1)
                  ]
    for point, char in grid.items():
        text_array[point[1] - size[1]][point[0] - size[0]] = char

    return "\n".join("".join(text_line) for text_line in text_array)


if __name__ == "__main__":
    input_text = sys.stdin.read()

    grid = read_grid(input_text)
    size = size_of(grid)

    count = 0
    while True:
        try:
            count += 1
            drop(grid, size)
        except IndexError:
            print(count - 1)
            break

        # print("\33[H", grid_to_text(grid), sep="")
        # time.sleep(0.5)
