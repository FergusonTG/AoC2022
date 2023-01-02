

import sys


DIRECTION_LEFT = "<"
DIRECTION_RIGHT = ">"


class GotToBottom(StopIteration):
    ...


def shapes_iter():
    shapes = [["@@@@"],
              [" @ ", "@@@", " @ "],
              ["@@@", "  @", "  @"],
              ["@", "@", "@", "@"],
              ["@@", "@@"],
              ]
    while True:
        yield from shapes


def moves_iter(input_text):
    while True:
        yield from input_text


def detect_overlap(floor_base, floor_profile, rock_base, rock):
    for rownum, layer in enumerate(rock):
        floor_level = rock_base - floor_base + rownum
        print(f"{floor_level=}")

        if floor_level >= len(floor_profile):
            continue

        print(f"{rownum} |{layer}| |{floor_profile[floor_level]}|"
              )
        if any(r != " " and c != " " for r, c in zip(
            layer, floor_profile[floor_level])):
            return True
    return False


def move_rock(rock, direction):
    if direction == DIRECTION_RIGHT:
        if all(rocklayer[-1] == " " for rocklayer in rock):
            rock = [" " + rocklayer[:-1] for rocklayer in rock]
        return rock
    if direction == DIRECTION_LEFT:
        if all(rocklayer[0] == " " for rocklayer in rock):
            rock = [rocklayer[1:] + " " for rocklayer in rock]
        return rock
    raise ValueError("Not a valid direction.")


def new_rock(shape_source):
    rock = [("  " + rocklayer + "     ")[:7]
             for rocklayer in next(shape_source)
            ]
    return rock


def drop(floor, rock, rock_bottom):
    for height, layer in enumerate(rock[::-1], start=rock_bottom):
        # print(f"Dropping: {rock_bottom=}, {height=}, {layer=}, {floor=}")
        if any(cell != " " and floor_level == height
               for floor_level, cell in zip(floor, layer)
               ):
            break
    else:
        return rock_bottom - 1

    # print("Reached bottom")
    floor_top = max(floor)
    for height, layer in enumerate(rock[::-1], start=rock_bottom + 1):
        for column, cell in enumerate(layer):
            if cell != " ":
                floor[column] = height
    raise GotToBottom


def draw(floor_base, floor_profile, rock_base, rock_profile):
    def merge(string1, string2):
        return "".join(
            s1 if s1 != " " else s2 for s1, s2 in zip(string1, string2)
        )

    txt = []
    for n, l in enumerate(floor_profile, start=floor_base):
        txt.append(f"{n:-4}:" + l)
    for n in range(floor_base + len(floor_profile), rock_base + len(rock_profile) + 1):
        txt.append(f"{n:-4}:" + " " * len(floor_profile[0]))
    for n, l in enumerate(rock_profile):
        txt[rock_base + n - 1] = merge("     " + l, txt[rock_base + n - 1])

    print("\n".join(txt[::-1]))


if __name__ == "__main__":
    inpt = sys.stdin.read()

    TARGET_ROCK_COUNT = 3

    floor = 0
    profile = ["======="]

    shape = shapes_iter()
    move = moves_iter(inpt)
    rock_count = 0
    while rock_count < TARGET_ROCK_COUNT:
        rock, rock_bottom = new_rock(shape), max(floor) + 3
        rock_count += 1
        try:
            while True:
                direction = next(move)
                rock = move_rock(rock, direction)
                rock_bottom = drop(floor, rock, rock_bottom)

        except GotToBottom:
            print(f"{rock_count:-9}: {floor}")

    print(floor)
    print(max(floor))
