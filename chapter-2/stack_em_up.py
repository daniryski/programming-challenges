"""2.8.5 Stack 'em Up"""

RANKS = [
        '2', '3', '4', '5', '6', '7', '8', '9', '10',
        'Jack', 'Queen', 'King', 'Ace']
SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

cases = int(input())
_ = input()

for case in range(0, cases):
    n_shuffles = int(input())
    read_input = []

    while True:
        try:
            read_line = list(map(int, input().split()))

            if read_line:
                read_input.extend(read_line)

            else:
                break

        except EOFError:
            break

    shuffles = [read_input[i * 52 : (i + 1) * 52] for i in range(0, n_shuffles)]

    deck = list(range(0, 52))

    for shuffle in read_input[52 * n_shuffles :]:
        new_deck = []

        for index, shuffle_card in zip(range(0, 52), shuffles[shuffle - 1]):
            new_deck.append(deck[shuffle_card - 1])

        deck = new_deck

    if case > 0:
        print()

    for card in deck:
        print('{} of {}'.format(RANKS[card % 13], SUITS[card // 13]))
