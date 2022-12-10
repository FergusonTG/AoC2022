"""Part two solution: detect CRT output."""

import sys


class Monitor:
    """Monitor the CPU cycles."""

    def __init__(self):
        self.cycles = 0
        self.x_reg = 1
        self.total = 0

    def cycle(self):
        self.cycles += 1

        y_pos, x_pos = divmod(self.cycles - 1, 40)

        if x_pos == 0:
            y_pos += 1
            print()

        if self.x_reg - x_pos in (-1, 0, 1):
            print("#", end="")
        else:
            print(" ", end="")

    def addx(self, value):
        self.cycle()
        self.cycle()
        self.x_reg += value


if __name__ == "__main__":

    cpu = Monitor()

    for line in sys.stdin:

        if line.startswith("noop"):
            cpu.cycle()

        elif line.startswith("addx "):
            cpu.addx(int(line[5:], 10))

        else:
            raise RuntimeError("Invalid input: " + line)

    print()
