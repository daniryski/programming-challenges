"""2.8.1 Jolly Jumpers"""

while True:
    try:
        n, *sequence = map(int, input().split())

    except EOFError:
        break

    for i in range(0, n - 1):
        sequence[i] = abs(sequence[i + 1] - sequence[i])

    _ = sequence.pop()
    sequence.sort()

    if sequence == list(range(1, n)):
        print('Jolly')

    else:
        print('Not jolly')
