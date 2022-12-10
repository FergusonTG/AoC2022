"""Part one solution: detect CRT signals."""

import sys


class Monitor:
    """Monitor the CPU cycles."""

    def __init__(self):
        self.cycles = 0
        self.x_reg = 1
        self.total = 0

    def cycle(self):
        self.cycles += 1

        if self.cycles % 40 == 20:
            self.total += self.cycles * self.x_reg
            print(f"{self.cycles:4}: {self.x_reg:4}, {self.cycles * self.x_reg:4} -> {self.total:6}")

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
