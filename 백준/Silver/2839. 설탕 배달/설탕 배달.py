import sys

input = sys.stdin.readline

N = int(input())

dp = [float("inf")] * (N+1)

# dp[i]: i kg의 설탕을 배달하는 데 필요한 최소 봉지 개수

# 초기값 설정
if N >= 3:
    dp[3] = 1
if N >= 5:
    dp[5] = 1

# i kg를 만드는 방법은 2가지이다.
# 1) (i-3) kg를 만드는 방법에 3kg 봉지 추가
# 2) (i-5) kg를 만드는 방법에 5kg 봉지 추가

# dp[i]는 위 두 가지 경우 중, 3kg, 5kg를 추가한 경우에서 작은 것
# -> dp[i] = min(dp[i-3] + 1, dp[i-5] + 1)

# i를 6부터 N까지 증가시키면서 dp 테이블을 채운다
for i in range(6, N+1):
    # # dp[i-3] 이나 dp[i-5] 가 초기값이 아닌 경우에만 계산에 포함
    # if dp[i-3] != float("inf") or dp[i-5] != float("inf"):
    #     dp[i] = min(dp[i-3], dp[i-5]) + 1
    dp[i] = min(dp[i-3] + 1, dp[i-5] + 1)

if dp[N] == float("inf"):
    print(-1)
else:
    print(dp[N])

