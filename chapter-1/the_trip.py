"""1.6.3 The Trip"""

while True:
    n = int(input())

    if not n:
        break

    else:
        spent = []
        total_spent = int(0)

        for i in range(0, n):
            dollars, cents = map(int, input().split('.', maxsplit=1))
            in_cents = dollars * 100 + cents
            spent.append(in_cents)
            total_spent += in_cents

        avg = total_spent // n
        above_avg = total_spent % n

        payments = [x - avg for x in spent if x > avg]
        changed = sum(payments) - min(above_avg, len(payments))

        print('${:.2f}'.format(changed / 100))
