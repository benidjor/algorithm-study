import sys
import math

input = sys.stdin.readline

T = int(input())


def calculate(M, N, x, y):
    k = x
    while k <= math.lcm(M, N):
        if (k-1) % N + 1 == y:
            return k
        k += M
    return -1

for _ in range(T):
    M, N, x, y = map(int, input().split())
    answer = calculate(M, N, x, y)

    print(answer)


