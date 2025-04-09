import sys

N, M = map(int, sys.stdin.readline().split())
basket = [0] * N

for i in range(M):
    numbers = [int(x) for x in sys.stdin.readline().split()]
    start = numbers[0]
    end = numbers[1]
    
    for j in range(start-1, end):
        basket[j] = numbers[2]

print(*basket)