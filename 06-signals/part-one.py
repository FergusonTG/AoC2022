"""Detect a start token of four distinct characters.

>>> process_stream(bytearray(b"mjqjpqmgbljsphdztnvjfqwrcgsmlb"))
7
>>> process_stream(bytearray(b"bvwbjplbgvbhsrlpgdmjqwftvncz"))
5
>>> process_stream(bytearray(b"nppdvjthqldpwncqszvftbrmjlhg"))
6
>>> process_stream(bytearray(b"nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"))
10
>>> process_stream(bytearray(b"zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"))
11

"""

import sys


LENGTH_OF_MARKER = 4

def lpop(buffer, length=1):
    byt = buffer[:length]
    del buffer[:length]
    return byt

def uniq(buffer):
    for byt in range(len(buffer) - 1):
        if buffer[byt] in buffer[byt + 1:]:
            return False
    return True


def process_stream(inpt):
    """Read a stream until four distinct bytes found."""
    chars = bytearray(b' ') + bytearray(lpop(inpt, length=3))
    count = 3

    while not uniq(chars := chars[1:] + lpop(inpt)):
        count += 1

    count += 1
    return count


if __name__ == "__main__":
    inpt = bytearray(sys.stdin.buffer.read())
    count = process_stream(inpt)
    print(count)
