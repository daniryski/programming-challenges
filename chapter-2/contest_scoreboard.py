"""2.8.7 Contest Scoreboard"""

from collections import defaultdict
from operator import itemgetter


cases = int(input())
_ = input()

for case in range(0, cases):
    attempts = defaultdict(lambda: defaultdict(lambda: 0))
    solved = defaultdict(lambda: set())
    submissions = dict()

    while True:
        try:
            contestant, problem, time, submission = input().split(maxsplit=3)
            contestant, problem, time = map(int, (contestant, problem, time))

        except (EOFError, ValueError):
            break

        if contestant not in submissions:
            submissions[contestant] = (0, 0)

        if submission == 'C':
            if problem not in solved[contestant]:
                solved[contestant].add(problem)
                solved_problems, penalty = submissions[contestant]
                submissions[contestant] = (
                        solved_problems + 1,
                        penalty + time + 20 * attempts[contestant][problem])

        elif submission == 'I':
            if problem not in solved[contestant]:
                attempts[contestant][problem] += 1

    scoreboard = [(c, s, p) for (c, (s, p)) in submissions.items()]
    scoreboard.sort(key=itemgetter(0))
    scoreboard.sort(key=itemgetter(2))
    scoreboard.sort(key=itemgetter(1), reverse=True)

    if case > 0:
        print()

    for contestant, solved_problems, penalty in scoreboard:
        print(contestant, solved_problems, penalty)
