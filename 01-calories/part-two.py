"""Find the three elves with the most calories."""


INPUT_FILE = "./input"

def update_leaderboard(leaderboard, new_entry):
    "Recreate leaderboard in situ."""
    if leaderboard[2] > new_entry:
        return
    leaderboard[2] = new_entry
    if leaderboard[1] > new_entry:
        return
    leaderboard[1:3] = leaderboard[2:0:-1]
    if leaderboard[0] > new_entry:
        return
    leaderboard[0:2] = leaderboard[1::-1]


def most(inputs):
    """Find the elf with the most calories."""
    max_cals = [0, 0, 0]
    cals = 0
    for l in (l.strip() for l in inputs):
        if not l:
            update_leaderboard(max_cals, cals)
            # max_cals = sorted(max_cals + [cals], reverse=True)[0:3]
            cals = 0
        else:
            cals += int(l, 10)

    update_leaderboard(max_cals, cals)
    # max_cals = sorted(max_cals + [cals], reverse=True)[0:3]
    return max_cals


if __name__ == "__main__":
    inputs = [
        "1000",
        "2000",
        "3000",
        "",
        "4000",
        "",
        "5000",
        "6000",
        "",
        "7000",
        "8000",
        "9000",
        "",
        "10000",
    ]
    with open(INPUT_FILE, "r") as inputs:
        print(sum(most(inputs)))
