import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

numbers = list(range(1, N+1))

NCM = list(combinations(numbers, M))

for combination in NCM:
    print(" ".join(map(str, combination)))
