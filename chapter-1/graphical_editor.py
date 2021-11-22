"""1.6.5 Graphical Editor"""

import array


image = array.array('u', '')
width = 0
height = 0

while True:
    command = input()
    c = command[0]

    if c == 'I':
        _, width, height = command.split(maxsplit=2)
        width, height = map(int, (width, height))
        image = array.array('u', 'O' * (width + 1) * (height + 1))

    elif c == 'C':
        image = array.array('u', 'O' * (width + 1) * (height + 1))

    elif c == 'L':
        _, x, y, c = command.split(maxsplit=3)
        x, y = map(int, (x, y))

        image[y * width + x] = c

    elif c == 'V':
        _, x, y1, y2, c = command.split(maxsplit=4)
        x, y1, y2 = map(int, (x, y1, y2))
        y1, y2 = sorted((y1, y2))

        for y in range(y1, y2 + 1):
            image[y * width + x] = c

    elif c == 'H':
        _, x1, x2, y, c = command.split(maxsplit=4)
        x1, x2, y = map(int, (x1, x2, y))
        x1, x2 = sorted((x1, x2))

        for x in range(x1, x2 + 1):
            image[y * width + x] = c

    elif c == 'K':
        _, x1, y1, x2, y2, c = command.split(maxsplit=5)
        x1, y1, x2, y2 = map(int, (x1, y1, x2, y2))
        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                image[y * width + x] = c

    elif c == 'F':
        _, x, y, c = command.split(maxsplit=3)
        x, y = map(int, (x, y))

        old_c = image[y * width + x]
        r = set()
        stack = list()

        def fill(i, j):
            image[j * width + i] = c
            r.add((i, j))
            stack.append((i, j))

        fill(x, y)

        while stack:
            x1, y1 = stack.pop()
            adjacent = {
                    (x2, y2)
                    for x2, y2
                    in ((x1 - 1, y1), (x1 + 1, y1), (x1, y1 - 1), (x1, y1 + 1))
                    if 1 <= x2 <= width and 1 <= y2 <= height}

            for x2, y2 in adjacent - r:
                if image[y2 * width + x2] == old_c:
                    fill(x2, y2)

    elif c =='S':
        _, name = command.split(maxsplit=1)

        print(name)

        for y in range(1, height + 1):
            print(image[y * width + 1 : (y + 1) * width + 1].tounicode())

    elif c == 'X':
        break

    else:
        continue
