
import sys

RIGHT = (1, 0)
LEFT = (-1, 0)
UP = (0, 1)
DOWN = (0, -1)

NUM_ROPES = 10

class State:
    """Maintain statue of game."""

    def __init__(self):
        """Starting positions."""
        self.tail_trail = {(0, 0),}
        self.tail_pos = (0, 0)
        self.difference = (0, 0)


def sign(number):
    return -1 if number < 0 else 0 if number == 0 else +1


def add_vector(vector1, vector2):
    return (vector1[0] + vector2[0], vector1[1] + vector2[1])


def neg_vector(vector):
    return (-vector[0], -vector[1])


def catchup(head, tail):
    """Calculate new tail position, add to set."""

    difference = add_vector(head, neg_vector(tail))

    if all(abs(v) <= 1 for v in difference):
        # no action needed
        ...

    else:
        tail_move = (sign(difference[0]), sign(difference[1]))
        tail = add_vector(tail, tail_move)

    return tail


if __name__ == "__main__":

    ropes = [(0, 0)] * 10
    tail_trail = set()

    for line in sys.stdin.readlines():
        (direction, count) = ({"R": RIGHT, "L": LEFT, "U": UP, "D": DOWN}[line[0]],
                              int(line[2:], 10)
                              )
        for _ in range(count):
            ropes[0] = add_vector(ropes[0], direction)
            for num in range(1, NUM_ROPES):
                ropes[num] = catchup(ropes[num - 1], ropes[num])
            print(ropes)
            tail_trail.add(ropes[-1])

    print("/n", len(tail_trail))

