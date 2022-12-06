"""Check for one list contained in another."""

def compare_strings(string):
    """Detect if one range overlaps another

    >>> compare_strings('2-8', '3-4')
    True
    >>> compare_strings('3-4', '3-6')
    True
    >>> compare_strings('2-4', '6-8')
    False
    """
    string1, _, string2 = string.partition(",")

    beg1, end1 = (int(p) for p in string1.partition("-")[0:3:2])
    beg2, end2 = (int(p) for p in string2.partition("-")[0:3:2])

    return not (end1 < beg2 or beg1 > end2)


if __name__ == "__main__":
    # inputs = [
    #     "2-4,6-8",
    #     "2-3,4-5",
    #     "5-7,7-9",
    #     "2-8,3-7",
    #     "6-6,4-6",
    #     "2-6,4-8",
    # ]
    with open("./input", "r") as inputs:
        total = len([line for line in inputs if compare_strings(line.strip())])

    print(total)
