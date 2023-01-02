"""Obsipy library for searching for obsidian."""


def is_touching(rock1, rock2):
    """Check if two rocks have a face in common."""
    different = 0
    for pair in zip(rock1, rock2):
        if (diff := abs(pair[0] - pair[1])) > 1:
            return False
        different += diff
    return different == 1
