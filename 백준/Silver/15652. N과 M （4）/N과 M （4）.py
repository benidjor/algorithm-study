import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(range(1, N+1))

# 중복 조합 반환
for i in combinations_with_replacement(arr, r=M):
    print(*i)