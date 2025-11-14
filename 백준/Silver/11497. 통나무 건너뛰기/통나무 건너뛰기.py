import sys

input = sys.stdin.readline


T = int(input())

for _ in range(T):
    N = int(input())
    logs = list(map(int, input().split()))
    
    logs.sort()

    difficulty = 0
    for i in range(2, N):
        if logs[i] - logs[i-2] > difficulty:
            difficulty = logs[i] - logs[i-2]
    
    print(difficulty)