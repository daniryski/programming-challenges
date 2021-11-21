"""1.6.6 Interpreter"""

import array


def execute(register, memory):
    instruction_pointer = 0
    steps = 0

    while memory[instruction_pointer] != 100:
        instruction = memory[instruction_pointer] // 100
        x = (memory[instruction_pointer] % 100) // 10
        y = memory[instruction_pointer] % 10

        if instruction == 2:
            register[x] = y

        elif instruction == 3:
            register[x] = (register[x] + y) % 1000

        elif instruction == 4:
            register[x] = (register[x] * y) % 1000

        elif instruction == 5:
            register[x] = register[y]

        elif instruction == 6:
            register[x] = (register[x] + register[y]) % 1000

        elif instruction == 7:
            register[x] = (register[x] * register[y]) % 1000

        elif instruction == 8:
            register[x] = memory[register[y]]

        elif instruction == 9:
            memory[register[y]] = register[x]

        else:
            if register[y]:
                instruction_pointer = register[x] - 1

        instruction_pointer += 1
        steps += 1

    else:
        steps += 1

    return steps


n = int(input())
_ = input()

for case in range(0, n):
    register = array.array('l', [0] * 10)
    memory = array.array('l', [0] * 1000)

    i = 0

    while True:
        try:
            memory[i] = int(input())
            i += 1

        except (EOFError, ValueError):
            break

    if case > 0:
        print()

    print(execute(register, memory))
