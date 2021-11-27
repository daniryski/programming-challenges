"""2.8.6 Erdös numbers"""

from collections import defaultdict
import re


scenarios = int(input())

for scenario in range(1, scenarios + 1):
    papers, n_authors = map(int, input().split(maxsplit=1))
    authored_together = defaultdict(lambda: [])

    for _ in range(0, papers):
        authors = re.findall(r'\w+, [\w\.]+', input().split(':', 1)[0])

        for author in authors:
            for with_author in authors:
                if author != with_author:
                    authored_together[author].append(with_author)

    authors = []
    with_authors = ['Erdos, P.']
    erdos_number = 0
    erdos_numbers = defaultdict(lambda: 'infinity')

    while with_authors:
        authors = with_authors
        with_authors = []
        erdos_number += 1

        for author in authors:
            for with_author in authored_together[author]:
                if with_author not in erdos_numbers:
                    erdos_numbers[with_author] = erdos_number
                    with_authors.append(with_author)

    print('Scenario {}'.format(scenario))

    for _ in range(0, n_authors):
        author = input()
        print(author, erdos_numbers[author])
