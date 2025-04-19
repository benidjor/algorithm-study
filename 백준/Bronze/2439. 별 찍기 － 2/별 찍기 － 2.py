import sys

N = int(sys.stdin.readline().strip())

star_list = []

for i in range(1, N+1):
    print(" " * (N-i) + "*" * i)