"""1.6.1 The 3n + 1 problem"""

import functools


def cycle(n):
    while n > 1:
        yield n

        if n % 2:
            n = 3 * n + 1

        else:
            n //= 2

    else:
        yield 1


@functools.cache
def cycle_len(n):
    return sum(1 for _ in cycle(n))


while True:
    try:
        i, j = map(int, input().split(maxsplit=2))
        start, end = sorted((i, j))

        print(i, j, max(cycle_len(n) for n in range(start, end + 1)))

    except EOFError:
        break
