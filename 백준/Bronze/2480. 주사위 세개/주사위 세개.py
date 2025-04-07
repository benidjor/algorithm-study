import sys
from collections import Counter

a, b, c = map(int, sys.stdin.readline().split())

if a == b == c:
    money = 10000 + (a * 1000)
elif a != b and b != c and a != c:
    money = max(a, b, c) * 100
else:
    lst = [a, b, c]
    count = Counter(lst)
    count_dict = dict(count)
    num = [k for k, v in count_dict.items() if v == 2][0]
    money = 1000 + (num * 100)

print(money)