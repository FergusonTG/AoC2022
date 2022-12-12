"""Day 12; using Dijkstra's algorithm (or, at least, my best understanding of it)."""

import sys
import heapq
import time


UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

VERBOSE = False


class TwoDArray():
    """Manage a 2-d array without overhead of numpy."""

    def __init__(self, size, value=0):
        """Initialize to size.

        size: (x, y) tuple.
        """
        self.x_width, self.y_height = size
        self.array = [ [value for _ in range(size[0])] for _ in range(size[1])]

    @property
    def size(self):
        return (self.x_width, self.y_height)

    @classmethod
    def new_from(cls, array):
        """Create 2-d array from a list of lists."""
        # Sanity check
        if any(len(row) != len(array[0]) for row in array[1:]):
            raise ValueError("Not a rectangular array.")
        newarray = cls((len(array[0]), len(array)))
        newarray.array = array
        return newarray

    def peek(self, ref):
        """Return value at gridref ref."""
        return self.array[ref[1]][ref[0]]

    def poke(self, ref, value):
        """Set value at gridref ref."""
        if isinstance(self.array[ref[1]], str):
            row = self.array[ref[1]]
            self.array[ref[1]] = row[:ref[0]] + value+ row[ref[0] + 1:]
        else:
            self.array[ref[1]][ref[0]] = value

    def within(self, ref):
        """Check that ref exists within the grid."""
        return (0 <= ref[0] < self.x_width
                and 0 <= ref[1] < self.y_height
                )

    def find(self, target):
        """find target in 2-D array.

        return: (x, y) tuple such that self.peek(x, y) == target
        """
        for y, row in enumerate(self.array):
            if target in row:
                return (row.index(target), y)
        raise IndexError(f"cannot find target <{target}>")


def find_2d(lists, target):
    """find target in list of lists.

    return: (x, y) tuple such that lists[y][x] == target
    """
    for y, line in enumerate(lists):
        if target in line:
            return (line.index(target), y)
    raise IndexError(f"cannot find target <{target}>")


def setoff(size, source, direction):
    """Add a direction to a source."""
    dest = (source[0] + direction[0], source[1] + direction[1])
    if 0 <= dest[0] < size[0] and 0 <= dest[1] < size[1]:
        return dest
    raise IndexError("Destination off grid!")


def debug_display(distances):
    # print("\33[12;H", end="")
    print("\33[u", end="")   # restore cursor position
    print("\n".join(", ".join(f"{i:02}" for i in line)
                    for line in distances.array))
    time.sleep(1)


if __name__ == "__main__":

    heights = TwoDArray.new_from([line.strip() for line in sys.stdin])

    infinity = heights.x_width * heights.y_height + 1

    start = heights.find("S")
    end = heights.find("E")
    heights.poke(start, chr(ord('a') - 1))
    heights.poke(end, chr(ord('z') + 1))

    print(start, end)
    if VERBOSE:
        print("\33[s", end="")  # save cursor position

    distances = TwoDArray((heights.x_width, heights.y_height), infinity)
    current = start
    distances.poke(start, 0)

    unvisited = []
    heapq.heappush(unvisited, (0, current))

    while True:
        distance_so_far, current = heapq.heappop(unvisited)
        if current == end:
            print(f"Finished: {distance_so_far}")
            break

        current_height = heights.peek(current)

        for direction in (UP, DOWN, LEFT, RIGHT):
            try:
                nextcell = setoff(distances.size, current, direction)
            except IndexError:
                continue
            if heights.peek(nextcell) > chr(ord(current_height) + 1):
                continue

            if distances.peek(nextcell) > distance_so_far + 1:
                distances.poke(nextcell, distance_so_far + 1)
                heapq.heappush(unvisited, (distance_so_far + 1, nextcell))

        if VERBOSE:
            debug_display(distances)
