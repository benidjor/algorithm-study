import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())

times = sorted(list(map(int, input().split())))

# 누적합 계산
prefix_sum_arr = [0] * N
prefix_sum_arr[0] = times[0]

for i in range(1, N):
    prefix_sum_arr[i] = prefix_sum_arr[i-1] + times[i]

print(sum(prefix_sum_arr))