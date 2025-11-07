import sys

input = sys.stdin.readline
N = int(input())

mid = len(str(N)) // 2


left = list(str(N)[:mid])

right = list(str(N)[mid:])

left_sum = sum(map(int, left))
right_sum = sum(map(int, right))

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")
