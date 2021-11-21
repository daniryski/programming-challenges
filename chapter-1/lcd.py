"""1.6.4 LCD"""

import array


DIGITS = array.array('b', [
    1, 0, 1, 1, 0, 1, 1, 1, 1, 1,
    0b11, 0b01, 0b01, 0b01, 0b11, 0b10, 0b10, 0b01, 0b11, 0b11,
    0, 0, 1, 1, 1, 1, 1, 0, 1, 1,
    0b11, 0b01, 0b10, 0b01, 0b01, 0b01, 0b11, 0b01, 0b11, 0b01,
    1, 0, 1, 1, 0, 1, 1, 0, 1, 1])


def horizontal(position, digit, width):
    char = '-' if DIGITS[10 * position + digit] else ' '

    return ' ' + char * width + ' '


def vertical(position, digit, width):
    f = lambda lr: '|' if DIGITS[10 * position + digit] & lr else ' '

    return f(0b10) + ' ' * width + f(0b01)


while True:
    s, n = input().split(maxsplit=2)
    s = int(s)
    digits = list(map(int, n))

    if (s, n) == (0, '0'):
        break

    else:
        print(' '.join(horizontal(0, digit, s) for digit in digits))

        for _ in range(0, s):
            print(' '.join(vertical(1, digit, s) for digit in digits))

        print(' '.join(horizontal(2, digit, s) for digit in digits))

        for _ in range(0, s):
            print(' '.join(vertical(3, digit, s) for digit in digits))

        print(' '.join(horizontal(4, digit, s) for digit in digits))

        print()
