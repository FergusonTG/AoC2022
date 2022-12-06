"""Detect a start token of four distinct characters.

>>> process_stream(bytearray(b"mjqjpqmgbljsphdztnvjfqwrcgsmlb"))
19
>>> process_stream(bytearray(b"bvwbjplbgvbhsrlpgdmjqwftvncz"))
23
>>> process_stream(bytearray(b"nppdvjthqldpwncqszvftbrmjlhg"))
23
>>> process_stream(bytearray(b"nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"))
29
>>> process_stream(bytearray(b"zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"))
26

"""

import sys


LENGTH_OF_MARKER = 14
VERBOSE = False

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
    chars = bytearray(b' ') + bytearray(lpop(inpt, length=LENGTH_OF_MARKER - 1))
    count = LENGTH_OF_MARKER - 1

    while not uniq(chars := chars[1:] + lpop(inpt)):
        if VERBOSE:
            print(str(chars))
        count += 1

    if VERBOSE:
        print(str(chars))
    count += 1
    return count


if __name__ == "__main__":
    # VERBOSE = True
    inpt = bytearray(sys.stdin.buffer.read())
    count = process_stream(inpt)
    print(count)
