import sys

remainders = []
for _ in range(10):
    N = int(sys.stdin.readline().strip())
    remainder = N % 42
    remainders.append(remainder)

remainders_set = set(remainders)
print(len(remainders_set))