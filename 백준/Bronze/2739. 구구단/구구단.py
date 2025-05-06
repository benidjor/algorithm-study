import sys

N = int(sys.stdin.readline().strip())

for i in range(1, 10):
    ans = N*i
    print(f"{N} * {i} = {ans}")