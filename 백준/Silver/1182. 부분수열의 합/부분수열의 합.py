import sys
from itertools import combinations

input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

cnt = 0
for i in range(1, N+1):
    nCr = list(combinations(numbers, i))
    # print(f"{i}: {nCr}")
    # print(sum(nCr))
    
    for combination in nCr:
        # print(sum(combination))

        if sum(combination) == S:
            cnt += 1

print(cnt)