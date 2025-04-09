import sys

N, M = map(int, sys.stdin.readline().split())

basket = [i for i in range(1, N+1)]

for x in range(M):
    i, j = map(int, sys.stdin.readline().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

print(*basket)