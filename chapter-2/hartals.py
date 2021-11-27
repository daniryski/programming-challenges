"""2.8.3 Hartals"""

cases = int(input())

for case in range(0, cases):
    days = int(input())
    parties = int(input())
    hartals = [int(input()) for _ in range(0, parties)]

    skipped_days = 0

    for day in range(1, days + 1):
        week_day = day % 7

        if week_day == 6 or week_day == 0:
            continue

        else:
            skipped_days += any(day % hartal == 0 for hartal in hartals)

    print(skipped_days)
