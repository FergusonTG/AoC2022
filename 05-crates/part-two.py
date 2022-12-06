"""Find the tops of the crates after the crane driver has done her thing."""

import sys
import re


def piles(inputs):
    """Create the initial piles."""

    key_line = inputs.index("") - 1
    num_stacks = len(inputs[key_line].split())

    stacks = [[] for _ in range(num_stacks)]
    for line in inputs[key_line - 1::-1]:
        for stack in range(num_stacks):
            crate = line[stack * 4 + 1]
            if crate != " ":
                stacks[stack].append(crate)

    return stacks


def move_crate(stacks, src, dst, count):
    stacks[dst - 1].extend(stacks[src - 1][-count:])
    del stacks[src - 1][-count:]


if __name__ == "__main__":

    inputs = sys.stdin.buffer.read().decode(encoding="utf-8").splitlines()
    stacks = piles(inputs)

    pattern = re.compile(r"move (\d+) from (\d+) to (\d+)")
    start_line = inputs.index("") + 1
    for line in inputs[start_line:]:
        count, src, dst = (int(group, 10) for group in pattern.match(line).groups())
        move_crate(stacks, src, dst, count)

    top_of_stacks = "".join(stack[-1] for stack in stacks)
    print(top_of_stacks)
