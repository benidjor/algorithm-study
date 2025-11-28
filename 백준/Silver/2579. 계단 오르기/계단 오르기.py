import sys

input = sys.stdin.readline

N = int(input())

"""
max(dp[i-2], dp[i-3] + stairs[i-1]) + stairs[i]
"""

stairs = [0] + [int(input()) for _ in range(N)]

if N == 1:
    print(stairs[1])

else:
    dp = [0] * (N+1)

    dp[1] = stairs[1]
    dp[2] = dp[1] + stairs[2]

    for i in range(3, N+1):
        dp[i] = max(dp[i-2], dp[i-3] + stairs[i-1]) + stairs[i]
    
    print(dp[N])
