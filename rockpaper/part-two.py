"""Rock paper scissors strategy guide."""


SCORE_LINE = ["B X", "C Y", "A Z", "A X", "B Y", "C Z", "C X", "A Y", "B Z"]


def rewriteline(line):
    """Rewrite a line to give a proper scoreline.
    >>> rewriteline("A Y")
    'A X'
    >>> rewriteline("B X")
    'B X'
    >>> rewriteline("C Z")
    'C X'
    """
    win_lose = "XYZ".index(line[2]) - 1  # -1 lose, 0 draw, +1 win
    my_go = ("ABC".index(line[0]) + win_lose) % 3
    return line[0:2] + "XYZ"[my_go]


def scoreline(line):
    """Score a single line.
    >>> scoreline("A Y")
    8
    >>> scoreline("B X")
    1
    >>> scoreline("C Z")
    6
    """
    return 1 + SCORE_LINE.index(line)


if __name__ == "__main__":
    # inputs = [
    #     "A Y",
    #     "B X",
    #     "C Z",
    # ]

    with open("./input", "r") as inputs:
        total_score = sum(scoreline(rewriteline(line.strip())) for line in inputs)
        print(total_score)
