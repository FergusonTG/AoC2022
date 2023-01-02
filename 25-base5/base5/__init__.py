"""Funky base 5 conversion with - and == chars."""


CHARS = ['=', '-', '0', '1', '2']


def int_to_base5(number):
    """Convert number to base 5."""
    if number == 0:
        return "0"

    ret = ""
    while number:
        div, mod = divmod(number + 2, 5)
        ret = CHARS[mod] + ret
        number = div
    return ret


def base5_to_int(string):
    """Convert base5 back to number."""
    if string == "0":
        return 0
    ret = 0
    while string:
        char, string = string[0], string[1:]
        ret = ret * 5 + (CHARS.index(char) - 2)
    return ret
