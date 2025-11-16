import sys

input = sys.stdin.readline
N = int(input())

weights = [int(input()) for _ in range(N)]

sorted_weights = sorted(weights, reverse=True)

cur_weight = 0
max_weight = 0

for idx, weight in enumerate(sorted_weights):

    cur_weight = weight * (idx+1)
    max_weight = max(cur_weight, max_weight)

print(max_weight)
