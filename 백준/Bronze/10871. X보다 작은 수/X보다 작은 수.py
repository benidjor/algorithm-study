import sys

N, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
answer = []
for i in A:
    if i < X:
        answer.append(i)
print(*answer)

