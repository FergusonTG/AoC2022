"""Solve day 11 of AoC, chase the naughty monkeys."""


import sys
import math


NUMROUNDS = 10_000

class Monkey:
    """One monkey out of many."""

    def __init__(self, items, operation, test, iftrue, iffalse):
        self.items = items
        self.operation = operation
        self.test = test
        self.iftrue = iftrue
        self.iffalse = iffalse
        self.inspections = 0

    def throw(self):
        """Inspect an item and return where/ what to throw."""
        if not self.items:
            return IndexError("No items left")
        worry = self.items[0]
        self.items = self.items[1:]
        worry = self.operation(worry)
        worry = worry % MAGICNUMBER
        self.inspections += 1

        return (self.iftrue if worry % self.test == 0 else self.iffalse,
                worry
                )

    def __iter__(self):
        return self

    def __next__(self):
        if self.items:
            return self.items[0]
        else:
            raise StopIteration


def parse_input(stream):
    """Parse input line by line and return a Monkey."""
    line = next(stream).strip()
    if not line:
        line = next(stream).strip()

    if not line.startswith("Monkey "):
        raise ValueError(f"Invalid line {line}")
    print(line)

    line = next(stream)
    if not line.startswith("  Starting items: "):
        raise ValueError(f"Invalid line {line}")
    items = eval("[" + line[18:] + "]")

    line = next(stream)
    if not line.startswith("  Operation: new = "):
        raise ValueError(f"Invalid line {line}")
    operation = eval("lambda worry: " + line[19:].replace("old", "worry"))

    line = next(stream)
    if not line.startswith("  Test: divisible by "):
        raise ValueError(f"Invalid line {line}")
    test = int(line[21:], 10)

    line = next(stream)
    if not line.startswith("    If true: throw to monkey "):
        raise ValueError(f"Invalid line {line}")
    iftrue = int(line[29:], 10)

    line = next(stream)
    if not line.startswith("    If false: throw to monkey "):
        raise ValueError(f"Invalid line {line}")
    iffalse = int(line[30:], 10)

    return Monkey(items, operation, test, iftrue, iffalse)


MAGICNUMBER = 1


if __name__ == "__main__":
    inpt = sys.stdin

    monkeys = []
    while True:
        try:
            monkeys.append(parse_input(inpt))
        except ValueError as e:
            raise e
        except StopIteration:
            break

    print(f"There are {len(monkeys)} defined.")
    MAGICNUMBER = math.prod(monkey.test for monkey in monkeys)

    for num in range(NUMROUNDS):
        for monkey in monkeys:
            for _ in monkey:
                monkey2, item = monkey.throw()
                monkeys[monkey2].items.append(item)

        if num % 500 == 0:
            print(f"Round {num}")

    monkeys.sort(key=lambda simian: simian.inspections, reverse=True)
    print([monkey.inspections for monkey in monkeys])
    print(monkeys[0].inspections * monkeys[1].inspections)
