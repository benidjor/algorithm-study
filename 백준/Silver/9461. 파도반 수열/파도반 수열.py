import sys

input = sys.stdin.readline

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2


T = int(input())

for _ in range(T):
    N = int(input())

    for i in range(N+1):
        if i > 5:
            dp[i] = dp[i-5] + dp[i-1]
    
    print(dp[N])

