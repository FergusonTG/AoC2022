"""Part Two solution for day 7: filesystems."""

import sys
from pprint import pprint


VERBOSE = False
DISK_SIZE = 70_000_000
UPDATE_SIZE = 30_000_000


def cd(target):
    """Update the global variable pwd."""
    global pwd
    if target == "/":
        pwd = "/"
    elif target == "..":
        pwd = pwd[: pwd.rindex("/", None, -1) + 1]
    else:
        pwd = pwd + target + "/"


if __name__ == "__main__":
    infile = sys.stdin
    pwd = "/"
    file_list = []
    folder_list = ["/"]
    listing = False

    for line in (line.strip() for line in infile):
        if VERBOSE:
            print(pwd, ">", line)  # noqa: E701

        if listing:
            if line.startswith("$"):
                listing = False

            elif line.startswith("dir"):
                folder_list.append(pwd + line[4:] + "/")
                if VERBOSE:
                    print(f"    found folder {line[4:]}")  # noqa: E701

            else:
                size, _, filename = line.partition(" ")
                file_list.append(
                    (
                        pwd + filename,
                        int(size, 10),
                    )
                )
                if VERBOSE:
                    print(f"    found file {filename}")  # noqa: E701

        if not listing:
            if line.startswith("$ cd"):
                cd(line[5:])
            if line.startswith("$ ls"):
                listing = True

    if VERBOSE:
        pprint(file_list)  # noqa: E701
    if VERBOSE:
        pprint(folder_list)  # noqa: E701

    folders = [
        (folder, sum(size for file, size in file_list if file.startswith(folder)))
        for folder in folder_list
    ]
    folders.sort(key=lambda f: f[1])

    space_needed = folders[-1][1] - DISK_SIZE + UPDATE_SIZE
    for (folder, size) in folders:
        if size >= space_needed:
            print((folder, size))
            break
