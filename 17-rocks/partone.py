

import sys
from pprint import pprint


DIRECTION_LEFT = "<"
DIRECTION_RIGHT = ">"

NUM_STACKS = 7

CHAR_AIR = ord(b'.')
CHAR_ROCK = ord(b'@')
CHAR_FALLEN = ord(b'#')
CHAR_WALL = ord(b'|')
CHAR_FLOOR = ord(b'=')


class GotToBottom(StopIteration):
    ...


def shapes_iter():
    shapes = [[b'@', b'@', b'@', b'@'],
              [b' @ ', b'@@@', b' @ '],
              [b"@  ", b"@  ", b"@@@"],
              [b"@@@@"],
              [b"@@", b"@@"],
              ]
    while True:
        yield from shapes


def moves_iter(input_text):
    while True:
        yield from input_text


def detect_overlap(floor_base, floor_profile, rock, rock_left, rock_base):
    """Set up the grid and check for overlap."""
    max_stack = max(len(stack) for stack in floor_profile)
    max_rock = rock_base + max(len(col) for col in rock)
    grid_len = max(max_stack, max_rock)

    grid = [bytearray(CHAR_WALL for _ in range(grid_len))]
    for stack in floor_profile:
        grid += [bytearray(stack).ljust(grid_len)]
    grid += [grid[0]]

    for s, col in enumerate(rock):
        stack = grid[1 + rock_left + s]
        # col is a column slice of rock; stack is a column of air
        # print(f"stack {s}: compare {stack} with {col}")
        for c, char in enumerate(col):
            if char != CHAR_ROCK:
                continue

            # print(f"{stack[c + rock_base - floor_base]} at pos {c + rock_base - floor_base}")
            if stack[c + rock_base - floor_base] != CHAR_AIR:
                return True
    return False


def move_rock(floor_base, floor_profile, rock, rock_left, rock_base, direction):
    if direction == DIRECTION_RIGHT:
        new_rock_left = rock_left + 1
    elif direction == DIRECTION_LEFT:
        new_rock_left = rock_left - 1
    else:
        raise ValueError("Not a valid direction.")

    if detect_overlap(floor_base, floor_profile, rock, rock_left, rock_base):
        return  rock_left  # Don't update the position of the rock

    return new_rock_left


def drop_rock(floor_base, floor_profile, rock, rock_left, rock_base):
    """Drop the rock and see if it overlaps something."""
    new_rock_base = rock_base - 1
    if detect_overlap(floor_base, floor_profile, rock, rock_left, rock_base):
        print(f"Got to bottom: {floor_base=}, {rock_base=}")
        raise GotToBottom
    return new_rock_base


def freeze_rock(floor_base, floor_profile, rock, rock_left, rock_base):
    """Freeze the rock into the cave profile."""
    max_stack = max(len(stack) for stack in floor_profile)
    max_rock = rock_base + max(len(col) for col in rock)
    grid_len = max(max_stack, max_rock)

    print("Freezing... <brrr>")
    grid = []
    for stack in floor_profile:
        grid +=  [bytearray(stack).ljust(grid_len)]
    print('\n'.join(str(stack) for stack in grid))

    for s, col in enumerate(rock):
        stack = grid[s + rock_left]  # don't add 1, we're not using walls
        for c, char in enumerate(col):
            if char == CHAR_AIR:
                pass
            else:
                grid[s + rock_left][c + rock_base - floor_base] = ord('Y')

    return [bytes(stack.rstrip()) for stack in grid]


def draw(floor_base, floor_profile, rock, rock_left, rock_base):
    """Set up the grid and merge in the rock."""

    grid_len = max(len(stack) for stack in floor_profile) + 7  # tall enough?
    grid = [bytearray(124 for _ in range(grid_len))]
    for stack in floor_profile:
        grid += [(bytearray(stack) + bytearray([32] * grid_len))[:grid_len]]
    grid += [grid[0]]

    for s, col in enumerate(rock):
        for c, char in enumerate(col):
            if char == b"  ":
                continue

            stack = grid[s + rock_left + 1]
            stack[c + rock_base - floor_base] = char

    txt = [bytes(byt).decode(encoding="ascii") for byt in zip(*grid)]
    print("\n".join(txt[::-1]))


if __name__ == "__main__":
    inpt = sys.stdin.read()

    TARGET_ROCK_COUNT = 3

    # start from the bottom
    floor_base = 0
    # stacks are arranged in (7) byte strings
    profile = [bytes([CHAR_FLOOR])] * NUM_STACKS

    # infinite generator for shapes
    shape = shapes_iter()
    # infinite generator for right/left winds
    move = moves_iter(inpt)

    rock_count = 0
    while rock_count < TARGET_ROCK_COUNT:
        rock = next(shape)
        rock_left = 2
        rock_base = max(len(stack) + floor_base for stack in profile) + 3
        rock_count += 1
        # print(f"{rock=}")
        try:
            while True:
                print(f"{rock_base=}")
                direction = next(move)
                rock_left = move_rock(
                    floor_base, profile, rock, rock_left, rock_base, direction
                )
                rock_base = drop_rock(
                    floor_base, profile, rock, rock_left, rock_base
                )
                draw(
                    floor_base, profile, rock, rock_left, rock_base
                )
        except GotToBottom:
            print("Got to bottom: freezing now")
            rock_base += 1   # Don't go through the floor
            profile = freeze_rock(
                    floor_base, profile, rock, rock_left, rock_base
            )
            draw(
                floor_base, profile, rock, rock_left, rock_base
            )
            move_up_floor = min(len(stack) for stack in profile) - 1
            for stack in profile[::]:
                stack = stack[move_up_floor:]
            floor_base += move_up_floor

    print(f"Final tower: {floor_base + max(len(stack) for stack in profile)}")
