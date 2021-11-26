"""1.6.2 Minesweeper"""

import array
import itertools


FIELD = array.array('u', ['.'] * 100 * 100)


def adjacent_squares(i, j):
    return itertools.product(range(i - 1, i + 2), range(j - 1, j + 2))


def print_field(rows, columns):
    for i in range(0, rows):
        for j in range(0, columns):
            if FIELD[i * columns + j] == '*':
                print('*', end='')

            else:
                print(
                        sum(FIELD[x * columns + y] == '*'
                            for x, y
                            in adjacent_squares(i, j)
                            if 0 <= x < rows and 0 <= y < columns),
                        end='')

        print()


field_number = 0

while True:
    rows, columns = map(int, input().split(maxsplit=1))

    if (rows, columns) == (0, 0):
        break

    else:
        field_number += 1

        for i in range(0, rows):
            for j, c in zip(range(0, columns), input()):
                FIELD[i * columns + j] = c

        if field_number > 1:
            print()

        print(f'Field #{field_number}:')
        print_field(rows, columns)
