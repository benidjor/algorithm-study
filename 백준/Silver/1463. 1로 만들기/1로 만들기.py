import sys

input = sys.stdin.readline

N = int(input())

dp = [float("inf")] * (N+1)


for i in range(N+1):
    if i in [0, 1]:
        dp[i] = 0
        continue
    
    if i in [2, 3]:
        dp[i] = 1
        continue
    
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i])    

    if i % 3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])

print(dp[N])

