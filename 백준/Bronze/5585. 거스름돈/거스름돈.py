import sys

price = int(sys.stdin.readline())

changes_cnt = 0

money = 1000 - price
changes = [500, 100, 50, 10, 5, 1]

for change in changes:
    if money >= change:
        changes_cnt += (money // change)
        money %= change

print(changes_cnt)