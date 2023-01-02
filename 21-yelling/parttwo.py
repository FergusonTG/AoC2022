"""Work out the monkeys yelling."""

import sys
from pprint import pprint
import operator
import re


OPERATORS = {
    "+": {"op": operator.add, "inv": operator.sub,},
    "-": {"op": operator.sub, "inv": operator.add,},
    "*": {"op": operator.mul, "inv": operator.floordiv,},
    "/": {"op": operator.floordiv, "inv": operator.mul,},
    "=": {"op": operator.eq, "inv": None,},
}


class Node:
    def __init__(self, label, **kwds):
        self.label = label
        super().__init__(**kwds)


class ValueNode(Node):
    def __init__(self, value, **kwds):
        self.value = value
        super().__init__(**kwds)


class CalcNode(Node):
    def __init__(self, values, **kwds):
        self.operands = values[0::2]
        self.operator = OPERATORS[values[1]]


def is_int(object):
    return isinstance(object, int)


def is_str(object):
    return isinstance(object, str)


def read_input(lines):
    """Read the lines and make a dict."""
    base = {monkeyname: int(value) if value.isnumeric() else value.split()
            for monkeyname, value in [line.partition(": ")[0::2] for line in lines]
            }

    base["root"][1] = "="
    return base


def read_output(line):
    # line looks like ((.....) = xyz)
    def chopup(st):
        # break up line into three parts operand1, op, operand2
        if st.startswith("("):
            paren = st.rfind(")")
            assert paren > -1
            p1 = st[1:paren]
            op, _, p2 = st[paren + 1:].strip().partition(" ")
        elif st.endswith(")"):
            paren = st.find("(")
            assert paren > -1
            p1, _, op = st[:paren].strip().partition(" ")
            p2 = st[paren + 1:-1]
        else:
            p1, op, p2 = "", "", st

        return p1, op, p2

    if not(line.startswith("(") and line.endswith(")")):
        raise ValueError("Not a valid expression line")

    line = line[1:-1]
    expr, equals, target_str = chopup(line)
    if equals != "=" or not target_str.isnumeric():
        raise ValueError("Not an equality: " + line)

    target = int(target_str, 10)
    line = expr

    while line:
        operand1, op, operand2 = chopup(line)
        if operand1.isnumeric():
            target = OPERATORS[op]["inv"](target, int(operand1, 10))
            line = operand2

        elif operand2.isnumeric():
            target = OPERATORS[op]["inv"](target, int(operand2, 10))
            line = operand1

        else:
            raise RuntimeError(f"{operand1=}, {op=}, {operand2=}")

        print(line, "=", target)

    return expr, target


def traverse(base, start):
    """Recursive depth first traversal."""
    node = base[start]

    if start == 'humn':
        ret =  'humn'

    elif not is_int(node):
        lhs = traverse(base, node[0])
        rhs = traverse(base, node[2])
        if (is_str(lhs) and 'humn' in lhs
            or is_str(rhs) and 'humn' in rhs
            ):
            ret = f"({lhs} {node[1]} {rhs})"
        else:
            ret = OPERATORS[node[1]]["op"](lhs, rhs)

    else:
        ret = node

    return ret


if __name__ == "__main__":
    inpt = sys.stdin.read().splitlines()
    base = read_input(inpt)

    output = traverse(base, "root")
    read_output(output)
