

import sys


def compare(one, two):
    """Compare two lists element by element."""
    setup = ((2 if (type(one).__name__ == 'list') else 0)
             + (1 if (type(two).__name__ == 'list') else 0)
             )
    # print(f"Comparing {one} and {two}: {setup=}")

    if setup == 0:  # int & int
        return -1 if one < two else 0 if one == two else 1
    if setup == 1:  # int & list
        return compare([one], two)
    if setup == 2:  # list & int
        return compare(one, [two])

    for a, b in zip(one, two):
        cmp = compare(a, b)
        if cmp != 0:
            return cmp
    # print(f"Bottom of function: {one=}, {two=}")
    return 1 if len(one) > len(two) else 0 if len(one) == len(two) else -1


if __name__ == "__main__":
    pairs = sys.stdin.read().split("\n\n")
    # for i, p in enumerate(pairs, start=1):
    #     one, two = (eval(s) for s in p.split())
    #     cmp = compare(one, two)
    #     print(f"{i=} {cmp=}: {one}, {two}\n\n")

    ans =[i for i, p in enumerate(pairs, start=1)
          if compare(*(eval(s) for s in p.split())) == -1
          ]
    print(f"{ans=}, sum={sum(ans)}")
