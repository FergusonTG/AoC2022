"""Find the elf with the most calories."""


INPUT_FILE = "./input"

def most(inputs):
    """Find the elf with the most calories."""
    max_cals = 0
    cals = 0
    for l in (l.strip() for l in inputs):
        if not l:
            if cals > max_cals:
                max_cals = cals
            cals = 0
        else:
            cals += int(l, 10)

    return max_cals


if __name__ == "__main__":
    # inputs = [
    #     "1000",
    #     "2000",
    #     "3000",
    #     "",
    #     "4000",
    #     "",
    #     "5000",
    #     "6000",
    #     "",
    #     "7000",
    #     "8000",
    #     "9000",
    #     "",
    #     "10000",
    # ]
    with open(INPUT_FILE, "r") as inputs:
        print(most(inputs))
