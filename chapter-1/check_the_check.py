"""1.6.7 Check the Check"""

import array
import itertools


CHESSBOARD = array.array('u', '.' * 64)
game = 0


def check(fields, *pieces, jump=False):
    for file, rank in fields:
        if CHESSBOARD[8 * rank + file] in pieces:
            return True

        elif CHESSBOARD[8 * rank + file] == '.' or jump:
            continue

        else:
            break

    return False


def is_in_check(field):
    file, rank = field

    in_bounds = lambda f: 0 <= f[0] < 8 and 0 <= f[1] < 8

    if CHESSBOARD[8 * rank + file] == 'K':
        front = rank + 1
        pawn, knight, bishop, queen, rook = 'pnbqr'

    else:
        front = rank - 1
        pawn, knight, bishop, queen, rook = 'PNBQR'

    up_rank = range(rank + 1, 8)
    down_rank = range(rank - 1, -1, -1)
    left_file = range(file - 1, -1, -1)
    right_file = range(file + 1, 8)
    knight_fields = filter(
            in_bounds,
            itertools.chain(
                itertools.product([file - 2, file + 2], [rank - 1, rank + 1]),
                itertools.product([file - 1, file + 1], [rank - 2, rank + 2])))

    return any([
        check(filter(in_bounds, [(file - 1, front)]), pawn),
        check(filter(in_bounds, [(file + 1, front)]), pawn),
        check(zip(left_file, itertools.repeat(rank, 8)), queen, rook),
        check(zip(right_file, itertools.repeat(rank, 8)), queen, rook),
        check(zip(itertools.repeat(file, 8), up_rank), queen, rook),
        check(zip(itertools.repeat(file, 8), down_rank), queen, rook),
        check(zip(left_file, up_rank), bishop, queen),
        check(zip(left_file, down_rank), bishop, queen),
        check(zip(right_file, up_rank), bishop, queen),
        check(zip(right_file, down_rank), bishop, queen),
        check(knight_fields, knight, jump=True)])

while True:
    white_king = None
    black_king = None
    game += 1

    for rank in range(7, -1, -1):
        for file, c in zip(range(0, 8), input()):
            CHESSBOARD[8 * rank + file] = c

            if c == 'K':
                white_king = (file, rank)

            if c == 'k':
                black_king = (file, rank)

    _ = input()

    if white_king is None or black_king is None:
        break

    if is_in_check(white_king):
        checked_piece = 'white king'

    elif is_in_check(black_king):
        checked_piece = 'black king'

    else:
        checked_piece = 'no king'

    print('Game #{}: {} is in check.'.format(game, checked_piece))
