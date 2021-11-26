"""1.6.5 Graphical Editor"""

import array


image = array.array('u', '')
width = 0
height = 0

while True:
    command, *arguments = input().split()

    if command == 'I':
        width, height = map(int, arguments)
        image = array.array('u', 'O' * (width + 1) * (height + 1))

    elif command == 'C':
        image = array.array('u', 'O' * (width + 1) * (height + 1))

    elif command == 'L':
        x, y = map(int, arguments[:2])

        image[y * width + x] = arguments[2]

    elif command == 'V':
        x, y1, y2 = map(int, arguments[:3])
        y1, y2 = sorted((y1, y2))
        c = arguments[3]

        for y in range(y1, y2 + 1):
            image[y * width + x] = c

    elif command == 'H':
        x1, x2, y = map(int, arguments[:3])
        x1, x2 = sorted((x1, x2))
        c = arguments[3]

        for x in range(x1, x2 + 1):
            image[y * width + x] = c

    elif command == 'K':
        x1, y1, x2, y2 = map(int, arguments[:4])
        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))
        c = arguments[4]

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                image[y * width + x] = c

    elif command == 'F':
        x, y = map(int, arguments[:2])
        c = arguments[2]

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

    elif command =='S':
        name, = arguments
        print(name)

        for y in range(1, height + 1):
            print(image[y * width + 1 : (y + 1) * width + 1].tounicode())

    elif command == 'X':
        break

    else:
        continue
