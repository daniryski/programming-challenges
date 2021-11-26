"""1.6.8 Australian Voting"""

import itertools
from operator import itemgetter


cases = int(input())
_ = input()

for case in range(0, cases):
    n = int(input())

    all_candidates = [input() for _ in range(0, n)]
    candidates = set(range(0, n))
    ballot = []

    while True:
        try:
            line = input()

            if not line:
                break

            else:
                ballot.append([int(v) - 1 for v in line.split(maxsplit=n - 1)])

        except (EOFError, ValueError):
            break

    while True:
        counted_votes = sorted(
                ((candidate, len(list(votes)))
                    for candidate, votes
                    in itertools.groupby(sorted(b[0] for b in ballot))),
                key=itemgetter(1),
                reverse=True)
        _, strongest_vote = counted_votes[0]

        if all(vote == strongest_vote for _, vote in counted_votes):
            if case > 0:
                print()

            for candidate, _ in counted_votes:
                print(all_candidates[candidate])

            break

        elif len(counted_votes) < len(candidates):
            voted_for = {candidate for candidate, _ in counted_votes}

            for candidate in candidates - voted_for:
                for b in ballot:
                    b.remove(candidate)

            candidates = voted_for

        else:
            _, weakest_vote = counted_votes[-1]

            while counted_votes[-1][1] == weakest_vote:
                eliminated, _ = counted_votes.pop()
                candidates.remove(eliminated)

                for b in ballot:
                    b.remove(eliminated)
