import sys

N, M = map(int, sys.stdin.readline().split())

array_a = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
array_b = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

total_array = [
    [a + b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(array_a, array_b)
]

for row in total_array:
    print(*row)