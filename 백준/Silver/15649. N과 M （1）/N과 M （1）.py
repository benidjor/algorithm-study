import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())

numbers = list(range(1, N+1))

NPM = list(permutations(numbers, M))

for permutation in NPM:
    print(" ".join(map(str, permutation)))