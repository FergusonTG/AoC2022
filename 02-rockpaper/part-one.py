"""Rock paper scissors strategy guide."""


SCORE_LINE = ["B X", "C Y", "A Z", "A X", "B Y", "C Z", "C X", "A Y", "B Z"]


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
        total_score = sum(scoreline(line.strip()) for line in inputs)
        print(total_score)
