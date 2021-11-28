"""2.8.2 Poker Hands"""

import itertools


HAND_TYPES = [
        'high card', 'pair', 'two pairs', 'three cards',
        'straight', 'flush', 'full house', 'four cards', 'straight flush']


def rank_hand(hand):
    hand_ranks = sorted('23456789TJQKA'.index(rank) for rank, _ in hand)

    hand_type = 'high card'
    hand_rank = tuple(reversed(hand_ranks))

    for rank, group in itertools.groupby(hand_ranks):
        count = len(list(group))

        if count == 2:
            if hand_type == 'high card':
                hand_type = 'pair'
                hand_rank = rank, *(r for r in hand_rank if r != rank)

            elif hand_type == 'pair':
                hand_type = 'two pairs'
                hand_rank = rank, *(r for r in hand_rank if r != rank)

            elif hand_type == 'three cards':
                hand_type = 'full house'

        elif count == 3:
            if hand_type == 'high card':
                hand_type = 'three cards'
                hand_rank = (rank,)

            elif hand_type == 'pair':
                hand_type = 'full house'
                hand_rank = (rank,)

        elif count == 4:
            hand_type = 'four cards'
            hand_rank = (rank,)

    is_straight = hand_ranks == list(range(hand_ranks[0], hand_ranks[0] + 5))
    is_flush = len({ suit for _, suit in hand }) == 1

    if is_straight and is_flush:
        hand_type = 'straight flush'

    elif is_straight:
        hand_type = 'straight'

    elif is_flush:
        hand_type = 'flush'

    return (HAND_TYPES.index(hand_type), hand_rank)


while True:
    try:
        deal = input().split(maxsplit=9)

    except EOFError:
        break

    black_rank = rank_hand(deal[:5])
    white_rank = rank_hand(deal[5:])

    if black_rank > white_rank:
        print('Black wins.')

    elif white_rank > black_rank:
        print('White wins.')

    else:
        print("Tie.")
