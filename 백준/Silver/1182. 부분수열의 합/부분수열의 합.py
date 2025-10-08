import sys
from itertools import combinations

input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

cnt = 0
for i in range(1, N+1):
    nCr = combinations(numbers, i)
    
    for combination in nCr:

        if sum(combination) == S:
            cnt += 1

print(cnt)