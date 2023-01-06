"""Funky base 5 conversion with - and == chars."""


CHARS = ['=', '-', '0', '1', '2']
CH_TO_VAL = dict(zip(CHARS, range(-2, 3)))
VAL_TO_CH = {val: char for char, val in CH_TO_VAL.items()}


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


def add_base5(num1, num2):
    """Add two snafu numbers."""
    columns = max(len(num) for num in (num1, num2))
    num1, num2 = (num.rjust(columns, "0") for num in (num1, num2))
    print(num1, num2)

    carry = "0"
    ret = ""
    for dg1, dg2 in zip(reversed(num1), reversed(num2)):
        digit, carry = add_digit(dg1, dg2, carry)
        ret = digit + ret
    return ret


def add_digit(digit1, digit2, carry="0"):
    """Add digits, return tuple(sum, carry) as digits."""
    dg1, dg2, car = (CH_TO_VAL[char] for char in (digit1, digit2, carry))
    digit = (dg1 + dg2 + car + 2) % 5 - 2
    carry = (dg1 + dg2 + car - digit) // 5
    return VAL_TO_CH[digit], VAL_TO_CH[carry]
